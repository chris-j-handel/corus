// Pure port of Exhibit_ONE_Natural_Resolver object to statically-typed,
// JVM-executed (bytecode + JIT, "mixed mode") Java, plus the ring harness.
// Names follow the reference. Sparse maps keyed by sequencing, grown only for
// positions actually sounded. Increment only +/-1; only the sign surfaces.
import java.util.*;

public class RingPureV265 {
  // carry entry: [sequencing, morality, competency, re_attentioning]
  static int[][] biCoupling(int[][] commencing, int[][] accepted,
                            Map<Integer,Integer> surfaceOut) {
    Map<Integer,Integer> offering = new HashMap<>();
    for (int[] cr : commencing) offering.put(cr[0], cr[2]);

    List<int[]> biInv = new ArrayList<>();
    for (int[] f : accepted) if (f[1] != 0) biInv.add(new int[]{f[0], f[1]});
    for (int[] cr : commencing) {
      if (cr[1] > 0) biInv.add(new int[]{cr[0], -1});
      if (cr[1] < 0) biInv.add(new int[]{cr[0], 1});
    }
    Map<Integer,Integer> bma = new HashMap<>();
    for (int[] e : biInv) {
      if (e[1] > 0) bma.merge(e[0], 1, Integer::sum);
      if (e[1] < 0) bma.merge(e[0], -1, Integer::sum);
    }
    surfaceOut.clear();
    for (Map.Entry<Integer,Integer> e : bma.entrySet()) {
      int t = e.getValue();
      surfaceOut.put(e.getKey(), (t > 0) ? 1 : (t < 0 ? -1 : 0));
    }
    // re_commencing: aged carry first, then fresh surface overwrites; keyed by seq
    TreeMap<Integer,int[]> rc = new TreeMap<>();   // seq -> [mor,comp,reatt]
    for (int[] cr : commencing) {
      int r2 = cr[3] + 1;
      if (r2 <= 3 || (r2 == 4 && cr[2] > 0)) rc.put(cr[0], new int[]{cr[1], cr[2], r2});
    }
    for (Map.Entry<Integer,Integer> e : surfaceOut.entrySet()) {
      int s = e.getKey(), m = e.getValue();
      if (m != 0) rc.put(s, new int[]{m, 0 - offering.getOrDefault(s, 1), 0});
    }
    int[][] carries = new int[rc.size()][4];
    int i = 0;
    for (Map.Entry<Integer,int[]> e : rc.entrySet())
      carries[i++] = new int[]{e.getKey(), e.getValue()[0], e.getValue()[1], e.getValue()[2]};
    return carries;
  }

  public static void main(String[] args) {
    int N = Integer.parseInt(args[0]), turns = Integer.parseInt(args[1]), mode = Integer.parseInt(args[2]);
    Map<Integer,Integer> stands = new LinkedHashMap<>();   // only what stands
    for (int i = 0; i < N; i++) stands.put(i, (i % 2 == 0) ? 1 : -1);
    int[][] carry = new int[0][];
    StringBuilder out = new StringBuilder("[");
    for (int t = 0; t < turns; t++) {
      List<int[]> acc = new ArrayList<>();
      for (int i = 0; i < N; i++) {
        Integer L = stands.get(((i - 1) % N + N) % N);
        if (L != null && L != 0) acc.add(new int[]{i, L});
        if (mode == 1) { Integer R = stands.get((i + 1) % N);
                         if (R != null && R != 0) acc.add(new int[]{i, R}); }
      }
      Map<Integer,Integer> nsurf = new LinkedHashMap<>();
      carry = biCoupling(carry, acc.toArray(new int[0][]), nsurf);
      stands = new LinkedHashMap<>();                        // only what stands
      for (Map.Entry<Integer,Integer> e : nsurf.entrySet())
        if (e.getKey() >= 0 && e.getKey() < N) stands.put(e.getKey(), e.getValue());
      StringBuilder s = new StringBuilder("S=");
      for (int i = 0; i < N; i++) {                         // the trace's line, made here
        if (i > 0) s.append(",");
        s.append(stands.getOrDefault(i, 0));
      }
      s.append(" C=");
      for (int i = 0; i < carry.length; i++) {
        if (i > 0) s.append(";");
        s.append(carry[i][0]).append(":").append(carry[i][1]).append(":").append(carry[i][2]).append(":").append(carry[i][3]);
      }
      if (t > 0) out.append(",");
      out.append("\"").append(s).append("\"");
    }
    out.append("]");
    System.out.println(out);
  }
}
