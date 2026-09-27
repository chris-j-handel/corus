
# ---------------------------------------------------------------- the kinds of check
FAILURE_PROBES = {'T5', 'K26', 'H24', 'J11', 'P7', 'L29', 'HP11', 'RH16', 'LF8', 'GH15'}   # a failure confirmed at a nye link
BOUND_PROBES = {'F65', 'R55', 'N88', 'X43', 'X107'}                                       # the part of a nye link that holds
FIELD_PROBES = {'X146'}                                                                   # a field link's instance
EXACT_CHECKED = {'F21'}                                                                   # an exact link shown at the arithmetic
PART_ORDER = ['PART ONE · FOUNDATION', 'PART TWO · THE RESOLVER AT ITS NAMES', 'PART THREE · NUMBERS',
              'PART FOUR · MATHEMATICS', 'PART FIVE · NETWORKING', 'PART SIX · EQUILIBRIA',
              'PART SEVEN · EXPLAINING, NAMING AND THE METHOD', 'PART EIGHT · THE EXHIBITS OF OTHER WORKINGS']


class NeedsFile(FileNotFoundError):
    pass


def parse_args(argv):
    repos, verbose, limit = [], False, 120
    it = iter(argv)
    for a in it:
        if a == '--repo':
            repos.append(os.path.abspath(next(it)))
        elif a.startswith('--repo='):
            repos.append(os.path.abspath(a.split('=', 1)[1]))
        elif a == '--timeout':
            limit = int(next(it))
        elif a in ('-v', '--verbose'):
            verbose = True
        elif a in ('-h', '--help'):
            print(__doc__); sys.exit(0)
        else:
            sys.exit(f'unknown argument: {a}')
    return repos, verbose, limit


REPOS, VERBOSE, LIMIT = parse_args(sys.argv[1:])


class TimedOut(Exception):
    pass


def _alarm(signum, frame):
    raise TimedOut(f'no return within {LIMIT} s')


def timed(f):
    """Run f under the time limit, where the platform carries SIGALRM."""
    import signal
    if not hasattr(signal, 'SIGALRM'):
        return f()
    old = signal.signal(signal.SIGALRM, _alarm)
    signal.alarm(LIMIT)
    try:
        return f()
    finally:
        signal.alarm(0)
        signal.signal(signal.SIGALRM, old)
SEARCH = [HERE] + REPOS
FAKE_RESOLVER = os.path.join(os.sep, '<ccl>', 'resolver_v371.py')


def find(base):
    for d in SEARCH:
        p = os.path.join(d, base)
        if os.path.exists(p):
            return p
    return None


def resolver_source():
    md = find('Exhibit_ONE_Natural_Resolver_v371.md')
    if md:
        m = re.search(r'```python\n(.*?)```', open(md, encoding='utf-8').read(), re.S)
        if m:
            code = m.group(1)
            same = code == RESOLVER_COPY
            note = ('identical to the copy carried here' if same else
                    'DIFFERING from the copy carried here: the checks run at the Exhibit\'s code')
            return code, f'{os.path.basename(md)}, first python block ({note})'
    return RESOLVER_COPY, 'the copy carried in this file (Exhibit_ONE_Natural_Resolver_v371.md not found beside it)'


RESOLVER_SRC, RESOLVER_FROM = resolver_source()


def make_resolver_module():
    lines = RESOLVER_SRC.splitlines(True)
    linecache.cache[FAKE_RESOLVER] = (len(RESOLVER_SRC), None, lines, FAKE_RESOLVER)
    mod = types.ModuleType('resolver_v371')
    mod.__file__ = FAKE_RESOLVER
    exec(compile(RESOLVER_SRC, FAKE_RESOLVER, 'exec'), mod.__dict__)
    sys.modules['resolver_v371'] = mod
    return mod


def _ccl_path(path):
    """The path a part names, found beside the verifier or at a --repo folder."""
    base = os.path.basename(path)
    p = find(base)
    if p is None:
        raise NeedsFile(2, 'needs ' + base, base)
    return p


_real_open = open


def _ccl_open(path, *a, **k):
    if isinstance(path, str) and os.path.basename(path) == 'resolver_v371.py':
        return io.StringIO(RESOLVER_SRC)
    return _real_open(_ccl_path(path) if isinstance(path, str) else path, *a, **k)


def load_part(name):
    make_resolver_module()
    ns = {'__name__': 'ccl_' + name, '__file__': os.path.join(HERE, f'ccl_{name}_checks.py'),
          '__builtins__': __builtins__, 'open': _ccl_open, '_ccl_path': _ccl_path, 'RESOLVER_SRC': RESOLVER_SRC}
    exec(compile(PART_SOURCES[name], f'<ccl part {name}>', 'exec'), ns)
    checks = dict(ns['CHECKS'])
    for k, f in ns.get('FIELD_INSTANCES', {}).items():
        checks[k + ' (field instances)'] = f
    return checks


def link_of(cid):
    return re.match(r'[A-Z]+\d+', cid).group(0)


def kind_of(cid):
    lid = link_of(cid)
    if cid.endswith('_probe'):
        if lid in FAILURE_PROBES: return 'failure probe'
        if lid in BOUND_PROBES: return 'bound probe'
        if lid in FIELD_PROBES: return 'field probe'
        return 'probe'
    if cid.endswith('(field instances)'):
        return 'field instances'
    if lid in EXACT_CHECKED:
        return 'exact'
    return 'run'


def label_of(name, cid):
    if name == 'core':
        return PART_ORDER[0] if cid.startswith('F') else PART_ORDER[1]
    return PART_LABELS[name]


def sort_key(cid):
    lid = link_of(cid)
    return (ORDER.index(lid) if lid in ORDER else 10 ** 6, cid)


def run_all():
    rows = []
    for name in PART_SOURCES:
        try:
            checks = timed(lambda: load_part(name))
        except Exception as e:                       # a part that does not load fails whole
            rows.append((PART_LABELS[name] or PART_ORDER[0], f'<part {name}>', 'run', 'failed', f'the part does not load: {e!r}', 0))
            continue
        for cid in sorted(checks, key=sort_key):
            kind = kind_of(cid)
            t0 = time.time()
            try:
                ok = bool(timed(checks[cid]))
                if kind == 'failure probe':
                    status = 'confirmed failure' if ok else 'failed'
                    note = ('the failure stands (nye)' if ok else
                            'the probe no longer finds the failure: the file or the code changed; run the link again as run')
                else:
                    status = 'passed' if ok else 'failed'
                    note = ''
            except FileNotFoundError as e:
                status, note = 'skipped', 'needs ' + os.path.basename(str(e.filename or e))
            except ImportError as e:
                status, note = 'skipped', 'needs ' + (e.name or str(e))
            except Exception as e:
                status, note = 'failed', f'error: {e!r}'
            rows.append((label_of(name, cid), cid, kind, status, note, time.time() - t0))
    return rows


def wrap(prefix, items):
    return textwrap.fill(' '.join(items), width=100, initial_indent=prefix, subsequent_indent=' ' * len(prefix))


def main():
    t0 = time.time()
    print('Co-Chaining Logic Registry verifier v371 (Exhibit THIRTY)')
    print('Resolver:', RESOLVER_FROM)
    print('Files looked for at:', ', '.join(SEARCH))
    print()
    rows = run_all()
    tot = {'passed': 0, 'failed': 0, 'confirmed failure': 0, 'skipped': 0}
    for part in PART_ORDER:
        pr = [r for r in rows if r[0] == part]
        c = {s: sum(1 for r in pr if r[3] == s) for s in tot}
        for s in tot: tot[s] += c[s]
        head = f'{part}: {c["passed"]} passed, {c["failed"]} failed'
        if c['confirmed failure']: head += f', {c["confirmed failure"]} discrepancies reproduced at nye links'
        if c['skipped']: head += f', {c["skipped"]} skipped'
        print(head)
        if VERBOSE:
            for r in pr:
                desc = RUNS.get(r[1].replace(' (field instances)', ''), '')
                print(f'  {r[1]:<26} {r[3]:<18} [{r[2]}] {r[4]}')
                if desc: print(textwrap.fill(desc, 100, initial_indent=' ' * 6, subsequent_indent=' ' * 6))
        else:
            tag = {'run': '', 'field instances': '', 'exact': ' (exact)', 'bound probe': ' (nye bound, holding)',
                   'field probe': ' (field instance)', 'probe': ' (probe)'}
            passed = [r[1] + tag[r[2]] for r in pr if r[3] == 'passed']
            if passed: print(wrap('  passed: ', [p.replace(' ', ' ') for p in passed]).replace(' ', ' '))
            for r in pr:
                if r[3] == 'confirmed failure':
                    print(f'  discrepancy reproduced at nye link {link_of(r[1])}: {r[1]} returns True, {r[4]}')
            for r in pr:
                if r[3] == 'skipped':
                    print(f'  skipped {r[1]}: {r[4]}')
            for r in pr:
                if r[3] == 'failed':
                    print(f'  FAILED {r[1]}: {r[4] or "returns False"}')
                    desc = RUNS.get(r[1], '')
                    if desc: print(textwrap.fill('the run: ' + desc, 100, initial_indent=' ' * 6, subsequent_indent=' ' * 6))
        print()
    n = sum(tot.values())
    result = 'PASS' if tot['failed'] == 0 else 'FAIL'
    print(f'TOTAL: {n} checks, {tot["passed"]} passed, {tot["failed"]} failed, '
          f'{tot["confirmed failure"]} discrepancies reproduced at nye links, {tot["skipped"]} skipped, not run '
          f'({time.time() - t0:.1f} s). RESULT: {result}')
    print(f'Scope: RESULT covers the {n - tot["skipped"]} checks run, at the resolver named above and the arithmetic; '
          f'the {tot["skipped"]} skipped are unrun, and a discrepancy reproduced is a finding at its nye link, no verifying of a replacing claim.')
    return 0 if tot['failed'] == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
