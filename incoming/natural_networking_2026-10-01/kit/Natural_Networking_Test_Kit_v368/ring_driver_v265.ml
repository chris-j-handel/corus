(* OCaml ring harness on the faithful resolver_pure.ml (no modulus).
   Static typing, interpreted/bytecode via ocamlc — the fourth quadrant. *)
let () =
  let n = int_of_string Sys.argv.(1) in
  let turns = int_of_string Sys.argv.(2) in
  let mode = int_of_string Sys.argv.(3) in
  (* the ring holds only what stands: an association, sequencing -> sign *)
  let stands = ref (List.init n (fun i -> (i, if i mod 2 = 0 then 1 else -1))) in
  let at i = try List.assoc i !stands with Not_found -> 0 in
  let carry = ref ([] : Resolver_pure_v265.carry list) in
  let buf = Buffer.create 256 in
  Buffer.add_char buf '[';
  for t = 0 to turns - 1 do
    let accepted = ref ([] : Resolver_pure_v265.face list) in
    for i = n - 1 downto 0 do
      (if mode = 1 then begin
         let r = at ((i + 1) mod n) in
         if r <> 0 then accepted := { Resolver_pure_v265.sequencing = i; morality = r } :: !accepted
       end);
      let l = at ((i - 1 + n) mod n) in
      if l <> 0 then accepted := { Resolver_pure_v265.sequencing = i; morality = l } :: !accepted
    done;
    let (surf_faces, new_carry) = Resolver_pure_v265._1_self_coupling !carry !accepted in
    stands := List.filter_map                            (* only what stands *)
      (fun (f : Resolver_pure_v265.face) ->
         if f.sequencing >= 0 && f.sequencing < n then Some (f.sequencing, f.morality) else None)
      surf_faces;
    carry := new_carry;
    if t > 0 then Buffer.add_char buf ',';
    Buffer.add_string buf "\"S=";
    for i = 0 to n - 1 do                                (* the trace's line, made here *)
      if i > 0 then Buffer.add_char buf ',';
      Buffer.add_string buf (string_of_int (at i))
    done;
    Buffer.add_string buf " C=";
    List.iteri (fun i (c : Resolver_pure_v265.carry) ->
      if i>0 then Buffer.add_char buf ';';
      Buffer.add_string buf (Printf.sprintf "%d:%d:%d:%d" c.sequencing c.morality c.competency c.re_attentioning)) new_carry;
    Buffer.add_char buf '"'
  done;
  Buffer.add_char buf ']';
  print_string (Buffer.contents buf); print_newline ()
