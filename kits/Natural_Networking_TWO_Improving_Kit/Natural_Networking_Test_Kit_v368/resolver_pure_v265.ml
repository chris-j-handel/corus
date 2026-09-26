(* Pure port of Exhibit_ONE_Natural_Resolver_v241.py to statically-typed,
   interpreted OCaml. Names follow the reference. The sign-count is an
   association list keyed by [sequencing], holding only positions actually
   sounded and growing as the reference dict does, with no preallocation hint
   and no ceiling. Increment is only +/-1; only the sign surfaces. *)

type carry = { sequencing : int; morality : int; competency : int; re_attentioning : int }
type face  = { sequencing : int; morality : int }

(* sparse association from sequencing to a value, like dict.get(seq, dflt) *)
let assoc_get lst seq dflt =
  match List.assoc_opt seq lst with Some v -> v | None -> dflt

(* set, replacing the position if present, else prepending it *)
let assoc_set lst seq v =
  (seq, v) :: List.remove_assoc seq lst

let _1_self_coupling
    (commencing_co_agency : carry list)
    (accepted_bi_morality : face list)
  : face list * carry list =

  (* offering = {sequencing: competency} *)
  let offering =
    List.fold_left (fun acc (cr : carry) -> assoc_set acc cr.sequencing cr.competency)
      [] commencing_co_agency
  in

  (* bi_inversioning: accepted nonzero as-is; carry morality sign-inverted *)
  let bi_inversioning =
    (List.filter_map
       (fun (f : face) -> if f.morality <> 0 then Some (f.sequencing, f.morality) else None)
       accepted_bi_morality)
    @
    (List.filter_map
       (fun (cr : carry) ->
          if cr.morality > 0 then Some (cr.sequencing, -1)
          else if cr.morality < 0 then Some (cr.sequencing, 1) else None)
       commencing_co_agency)
  in

  (* bi_moral_attentioning: sparse sign-count, only +/-1 *)
  let bi_moral_attentioning =
    List.fold_left
      (fun acc (sequencing, morality) ->
         if morality > 0 then assoc_set acc sequencing (assoc_get acc sequencing 0 + 1)
         else if morality < 0 then assoc_set acc sequencing (assoc_get acc sequencing 0 - 1)
         else acc)
      [] bi_inversioning
  in

  (* bi_co_now: surface over what the releasing carries, sign only *)
  let bi_moral_sequencing =
    List.map (fun (sequencing, t) ->
        { sequencing; morality = (if t > 0 then 1 else if t < 0 then -1 else 0) })
      bi_moral_attentioning
  in

  (* re_commencing_co_agency: persist within the attentioning bound *)
  let re_commencing =
    List.fold_left
      (fun acc (cr : carry) ->
         let r2 = cr.re_attentioning + 1 in
         if r2 <= 3 || (r2 = 4 && cr.competency > 0)
         then (cr.sequencing, (cr.morality, cr.competency, r2))
              :: List.remove_assoc cr.sequencing acc
         else acc)
      [] commencing_co_agency
  in
  let re_commencing =
    List.fold_left
      (fun acc (f : face) ->
         if f.morality <> 0 then
           let off = assoc_get offering f.sequencing 1 in
           (f.sequencing, (f.morality, 0 - off, 0)) :: List.remove_assoc f.sequencing acc
         else acc)
      re_commencing bi_moral_sequencing
  in

  let carries =
    List.sort (fun (a, _) (b, _) -> compare a b) re_commencing
    |> List.map (fun (sequencing, (morality, competency, re_attentioning)) ->
        { sequencing; morality; competency; re_attentioning })
  in
  (bi_moral_sequencing, carries)
