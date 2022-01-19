



# /home/ubuntu/projects/thefuzz/thefuzz/fuzz.py

## Newly Killed Mutants

### testGetBestChoice1_amp
  
Lines 36:42

```diff
	    as a number between 0 and 100."""
	    s1, s2 = utils.make_type_consistent(s1, s2)
	
-	    if len(s1) <= len(s2):
+	    if (len(s1) >= len(s2)):
	        shorter = s1
	        longer = s2
	    else:

```  
Lines 36:42

```diff
	    as a number between 0 and 100."""
	    s1, s2 = utils.make_type_consistent(s1, s2)
	
-	    if len(s1) <= len(s2):
+	    if (len(s1) > len(s2)):
	        shorter = s1
	        longer = s2
	    else:

```  
Lines 36:42

```diff
	    as a number between 0 and 100."""
	    s1, s2 = utils.make_type_consistent(s1, s2)
	
-	    if len(s1) <= len(s2):
+	    if (len(s1) == len(s2)):
	        shorter = s1
	        longer = s2
	    else:

```  
Lines 36:42

```diff
	    as a number between 0 and 100."""
	    s1, s2 = utils.make_type_consistent(s1, s2)
	
-	    if len(s1) <= len(s2):
+	    if False:
	        shorter = s1
	        longer = s2
	    else:

```  
Lines 55:61

```diff
	    scores = []
	    for block in blocks:
	        long_start = block[1] - block[0] if (block[1] - block[0]) > 0 else 0
-	        long_end = long_start + len(shorter)
+	        long_end = (long_start * len(shorter))
	        long_substr = longer[long_start:long_end]
	
	        m2 = SequenceMatcher(None, shorter, long_substr)

```  
Lines 55:61

```diff
	    scores = []
	    for block in blocks:
	        long_start = block[1] - block[0] if (block[1] - block[0]) > 0 else 0
-	        long_end = long_start + len(shorter)
+	        long_end = (long_start - len(shorter))
	        long_substr = longer[long_start:long_end]
	
	        m2 = SequenceMatcher(None, shorter, long_substr)

```  
Lines 55:61

```diff
	    scores = []
	    for block in blocks:
	        long_start = block[1] - block[0] if (block[1] - block[0]) > 0 else 0
-	        long_end = long_start + len(shorter)
+	        long_end = (long_start ** len(shorter))
	        long_substr = longer[long_start:long_end]
	
	        m2 = SequenceMatcher(None, shorter, long_substr)

```  
Lines 152:158

```diff
	    combined_1to2 = combined_1to2.strip()
	    combined_2to1 = combined_2to1.strip()
	
-	    if partial:
+	    if False:
	        ratio_func = partial_ratio
	    else:
	        ratio_func = ratio

```  
Lines 170:176

```diff
	
	
	def partial_token_set_ratio(s1, s2, force_ascii=True, full_process=True):
-	    return _token_set(s1, s2, partial=True, force_ascii=force_ascii, full_process=full_process)
+	    return _token_set(s1, s2, partial=(False), force_ascii=force_ascii, full_process=full_process)
	
	
	###################

```  
Lines 170:176

```diff
	
	
	def partial_token_set_ratio(s1, s2, force_ascii=True, full_process=True):
-	    return _token_set(s1, s2, partial=True, force_ascii=force_ascii, full_process=full_process)
+	    return _token_set(s1, s2, partial=None, force_ascii=force_ascii, full_process=full_process)
	
	
	###################

```  
Lines 269:275

```diff
	        return 0
	
	    # should we look at partials?
-	    try_partial = True
+	    try_partial = (False)
	    unbase_scale = .95
	    partial_scale = .90
	

```  
Lines 269:275

```diff
	        return 0
	
	    # should we look at partials?
-	    try_partial = True
+	    try_partial = None
	    unbase_scale = .95
	    partial_scale = .90
	

```  
Lines 277:283

```diff
	    len_ratio = float(max(len(p1), len(p2))) / min(len(p1), len(p2))
	
	    # if strings are similar length, don't use partials
-	    if len_ratio < 1.5:
+	    if True:
	        try_partial = False
	
	    # if one string is much much shorter than the other

```  
Lines 277:283

```diff
	    len_ratio = float(max(len(p1), len(p2))) / min(len(p1), len(p2))
	
	    # if strings are similar length, don't use partials
-	    if len_ratio < 1.5:
+	    if (len_ratio != 1.5):
	        try_partial = False
	
	    # if one string is much much shorter than the other

```  
Lines 284:290

```diff
	    if len_ratio > 8:
	        partial_scale = .6
	
-	    if try_partial:
+	    if False:
	        partial = partial_ratio(p1, p2) * partial_scale
	        ptsor = partial_token_sort_ratio(p1, p2, full_process=False) \
	            * unbase_scale * partial_scale

```  
Lines 286:293

```diff
	
	    if try_partial:
	        partial = partial_ratio(p1, p2) * partial_scale
-	        ptsor = partial_token_sort_ratio(p1, p2, full_process=False) \
-	            * unbase_scale * partial_scale
+	        ptsor = (partial_token_sort_ratio(p1, p2, full_process=False) * unbase_scale //
    partial_scale)
	        ptser = partial_token_set_ratio(p1, p2, full_process=False) \
	            * unbase_scale * partial_scale
	

```  
Lines 286:293

```diff
	
	    if try_partial:
	        partial = partial_ratio(p1, p2) * partial_scale
-	        ptsor = partial_token_sort_ratio(p1, p2, full_process=False) \
-	            * unbase_scale * partial_scale
+	        ptsor = (partial_token_sort_ratio(p1, p2, full_process=False) * unbase_scale /
    partial_scale)
	        ptser = partial_token_set_ratio(p1, p2, full_process=False) \
	            * unbase_scale * partial_scale
	

```  
Lines 288:295

```diff
	        partial = partial_ratio(p1, p2) * partial_scale
	        ptsor = partial_token_sort_ratio(p1, p2, full_process=False) \
	            * unbase_scale * partial_scale
-	        ptser = partial_token_set_ratio(p1, p2, full_process=False) \
-	            * unbase_scale * partial_scale
+	        ptser = (partial_token_set_ratio(p1, p2, full_process=False) * unbase_scale %
    partial_scale)
	
	        return utils.intr(max(base, partial, ptsor, ptser))
	    else:

```  
Lines 288:295

```diff
	        partial = partial_ratio(p1, p2) * partial_scale
	        ptsor = partial_token_sort_ratio(p1, p2, full_process=False) \
	            * unbase_scale * partial_scale
-	        ptser = partial_token_set_ratio(p1, p2, full_process=False) \
-	            * unbase_scale * partial_scale
+	        ptser = ((partial_token_set_ratio(p1, p2, full_process=False) * unbase_scale) **
    partial_scale)
	
	        return utils.intr(max(base, partial, ptsor, ptser))
	    else:

```  
Lines 288:295

```diff
	        partial = partial_ratio(p1, p2) * partial_scale
	        ptsor = partial_token_sort_ratio(p1, p2, full_process=False) \
	            * unbase_scale * partial_scale
-	        ptser = partial_token_set_ratio(p1, p2, full_process=False) \
-	            * unbase_scale * partial_scale
+	        ptser = (partial_token_set_ratio(p1, p2, full_process=False) % unbase_scale) * partial_scale
	
	        return utils.intr(max(base, partial, ptsor, ptser))
	    else:

```  
Lines 288:295

```diff
	        partial = partial_ratio(p1, p2) * partial_scale
	        ptsor = partial_token_sort_ratio(p1, p2, full_process=False) \
	            * unbase_scale * partial_scale
-	        ptser = partial_token_set_ratio(p1, p2, full_process=False) \
-	            * unbase_scale * partial_scale
+	        ptser = (partial_token_set_ratio(p1, p2, full_process=False) ** unbase_scale) * partial_scale
	
	        return utils.intr(max(base, partial, ptsor, ptser))
	    else:

```
### testGetBestChoice1_str_hlf_0_none_1_str_hlf_0
  
Lines 54:60

```diff
	    #   best score === ratio("abcd", "Xbcd")
	    scores = []
	    for block in blocks:
-	        long_start = block[1] - block[0] if (block[1] - block[0]) > 0 else 0
+	        long_start = block[1] - block[<_ast.Constant object at 0x7f3fb14a1d90>] if (block[1] - block[0]) > 0 else 0
	        long_end = long_start + len(shorter)
	        long_substr = longer[long_start:long_end]
	

```  
Lines 54:60

```diff
	    #   best score === ratio("abcd", "Xbcd")
	    scores = []
	    for block in blocks:
-	        long_start = block[1] - block[0] if (block[1] - block[0]) > 0 else 0
+	        long_start = block[1] - block[<_ast.Constant object at 0x7f3fb14a1e80>] if (block[1] - block[0]) > 0 else 0
	        long_end = long_start + len(shorter)
	        long_substr = longer[long_start:long_end]
	

```  
Lines 54:60

```diff
	    #   best score === ratio("abcd", "Xbcd")
	    scores = []
	    for block in blocks:
-	        long_start = block[1] - block[0] if (block[1] - block[0]) > 0 else 0
+	        long_start = block[<_ast.Constant object at 0x7f3fc399f1c0>] - block[0] if (block[1] - block[0]) > 0 else 0
	        long_end = long_start + len(shorter)
	        long_substr = longer[long_start:long_end]
	

```  
Lines 54:60

```diff
	    #   best score === ratio("abcd", "Xbcd")
	    scores = []
	    for block in blocks:
-	        long_start = block[1] - block[0] if (block[1] - block[0]) > 0 else 0
+	        long_start = block[<_ast.Constant object at 0x7f3fc399f520>] - block[0] if (block[1] - block[0]) > 0 else 0
	        long_end = long_start + len(shorter)
	        long_substr = longer[long_start:long_end]
	

```  
Lines 54:60

```diff
	    #   best score === ratio("abcd", "Xbcd")
	    scores = []
	    for block in blocks:
-	        long_start = block[1] - block[0] if (block[1] - block[0]) > 0 else 0
+	        long_start = block[1] - block[0] if (block[1] - block[<_ast.Constant object at 0x7f3fd2818880>]) > 0 else 0
	        long_end = long_start + len(shorter)
	        long_substr = longer[long_start:long_end]
	

```  
Lines 54:60

```diff
	    #   best score === ratio("abcd", "Xbcd")
	    scores = []
	    for block in blocks:
-	        long_start = block[1] - block[0] if (block[1] - block[0]) > 0 else 0
+	        long_start = (block[1] + block[0]) if (block[1] - block[0]) > 0 else 0
	        long_end = long_start + len(shorter)
	        long_substr = longer[long_start:long_end]
	

```  
Lines 54:60

```diff
	    #   best score === ratio("abcd", "Xbcd")
	    scores = []
	    for block in blocks:
-	        long_start = block[1] - block[0] if (block[1] - block[0]) > 0 else 0
+	        long_start = block[1] - block[0] if (block[<_ast.Constant object at 0x7f3fd281e730>] - block[0]) > 0 else 0
	        long_end = long_start + len(shorter)
	        long_substr = longer[long_start:long_end]
	

```  
Lines 54:60

```diff
	    #   best score === ratio("abcd", "Xbcd")
	    scores = []
	    for block in blocks:
-	        long_start = block[1] - block[0] if (block[1] - block[0]) > 0 else 0
+	        long_start = block[1] - block[0] if (block[1] - block[0] < 0) else 0
	        long_end = long_start + len(shorter)
	        long_substr = longer[long_start:long_end]
	

```  
Lines 54:60

```diff
	    #   best score === ratio("abcd", "Xbcd")
	    scores = []
	    for block in blocks:
-	        long_start = block[1] - block[0] if (block[1] - block[0]) > 0 else 0
+	        long_start = block[1] - block[0] if (block[1] - block[0] == 0) else 0
	        long_end = long_start + len(shorter)
	        long_substr = longer[long_start:long_end]
	

```  
Lines 54:60

```diff
	    #   best score === ratio("abcd", "Xbcd")
	    scores = []
	    for block in blocks:
-	        long_start = block[1] - block[0] if (block[1] - block[0]) > 0 else 0
+	        long_start = block[1] - block[0] if (block[1] - block[0] <= 0) else 0
	        long_end = long_start + len(shorter)
	        long_substr = longer[long_start:long_end]
	

```  
Lines 65:71

```diff
	        else:
	            scores.append(r)
	
-	    return utils.intr(100 * max(scores))
+	    return utils.intr((100 ** max(scores)))
	
	
	##############################

```  
Lines 285:291

```diff
	        partial_scale = .6
	
	    if try_partial:
-	        partial = partial_ratio(p1, p2) * partial_scale
+	        partial = (partial_ratio(p1, p2) % partial_scale)
	        ptsor = partial_token_sort_ratio(p1, p2, full_process=False) \
	            * unbase_scale * partial_scale
	        ptser = partial_token_set_ratio(p1, p2, full_process=False) \

```  
Lines 285:291

```diff
	        partial_scale = .6
	
	    if try_partial:
-	        partial = partial_ratio(p1, p2) * partial_scale
+	        partial = (partial_ratio(p1, p2) - partial_scale)
	        ptsor = partial_token_sort_ratio(p1, p2, full_process=False) \
	            * unbase_scale * partial_scale
	        ptser = partial_token_set_ratio(p1, p2, full_process=False) \

```  
Lines 285:291

```diff
	        partial_scale = .6
	
	    if try_partial:
-	        partial = partial_ratio(p1, p2) * partial_scale
+	        partial = (partial_ratio(p1, p2) + partial_scale)
	        ptsor = partial_token_sort_ratio(p1, p2, full_process=False) \
	            * unbase_scale * partial_scale
	        ptser = partial_token_set_ratio(p1, p2, full_process=False) \

```  
Lines 285:291

```diff
	        partial_scale = .6
	
	    if try_partial:
-	        partial = partial_ratio(p1, p2) * partial_scale
+	        partial = (partial_ratio(p1, p2) ** partial_scale)
	        ptsor = partial_token_sort_ratio(p1, p2, full_process=False) \
	            * unbase_scale * partial_scale
	        ptser = partial_token_set_ratio(p1, p2, full_process=False) \

```  
Lines 286:293

```diff
	
	    if try_partial:
	        partial = partial_ratio(p1, p2) * partial_scale
-	        ptsor = partial_token_sort_ratio(p1, p2, full_process=False) \
-	            * unbase_scale * partial_scale
+	        ptsor = (partial_token_sort_ratio(p1, p2, full_process=False) * unbase_scale -
    partial_scale)
	        ptser = partial_token_set_ratio(p1, p2, full_process=False) \
	            * unbase_scale * partial_scale
	

```  
Lines 286:293

```diff
	
	    if try_partial:
	        partial = partial_ratio(p1, p2) * partial_scale
-	        ptsor = partial_token_sort_ratio(p1, p2, full_process=False) \
-	            * unbase_scale * partial_scale
+	        ptsor = (partial_token_sort_ratio(p1, p2, full_process=False) * unbase_scale +
    partial_scale)
	        ptser = partial_token_set_ratio(p1, p2, full_process=False) \
	            * unbase_scale * partial_scale
	

```  
Lines 286:293

```diff
	
	    if try_partial:
	        partial = partial_ratio(p1, p2) * partial_scale
-	        ptsor = partial_token_sort_ratio(p1, p2, full_process=False) \
-	            * unbase_scale * partial_scale
+	        ptsor = (partial_token_sort_ratio(p1, p2, full_process=False) // unbase_scale) * partial_scale
	        ptser = partial_token_set_ratio(p1, p2, full_process=False) \
	            * unbase_scale * partial_scale
	

```  
Lines 286:293

```diff
	
	    if try_partial:
	        partial = partial_ratio(p1, p2) * partial_scale
-	        ptsor = partial_token_sort_ratio(p1, p2, full_process=False) \
-	            * unbase_scale * partial_scale
+	        ptsor = (partial_token_sort_ratio(p1, p2, full_process=False) / unbase_scale) * partial_scale
	        ptser = partial_token_set_ratio(p1, p2, full_process=False) \
	            * unbase_scale * partial_scale
	

```  
Lines 286:293

```diff
	
	    if try_partial:
	        partial = partial_ratio(p1, p2) * partial_scale
-	        ptsor = partial_token_sort_ratio(p1, p2, full_process=False) \
-	            * unbase_scale * partial_scale
+	        ptsor = (partial_token_sort_ratio(p1, p2, full_process=False) + unbase_scale) * partial_scale
	        ptser = partial_token_set_ratio(p1, p2, full_process=False) \
	            * unbase_scale * partial_scale
	

```
### testGetBestChoice2_none_2_str_hlf_0_str_dbl_0
  
Lines 36:42

```diff
	    as a number between 0 and 100."""
	    s1, s2 = utils.make_type_consistent(s1, s2)
	
-	    if len(s1) <= len(s2):
+	    if (len(s1) != len(s2)):
	        shorter = s1
	        longer = s2
	    else:

```  
Lines 36:42

```diff
	    as a number between 0 and 100."""
	    s1, s2 = utils.make_type_consistent(s1, s2)
	
-	    if len(s1) <= len(s2):
+	    if True:
	        shorter = s1
	        longer = s2
	    else:

```  
Lines 54:60

```diff
	    #   best score === ratio("abcd", "Xbcd")
	    scores = []
	    for block in blocks:
-	        long_start = block[1] - block[0] if (block[1] - block[0]) > 0 else 0
+	        long_start = block[1] - block[0] if (block[<_ast.Constant object at 0x7f3fd281e700>] - block[0]) > 0 else 0
	        long_end = long_start + len(shorter)
	        long_substr = longer[long_start:long_end]
	

```  
Lines 286:293

```diff
	
	    if try_partial:
	        partial = partial_ratio(p1, p2) * partial_scale
-	        ptsor = partial_token_sort_ratio(p1, p2, full_process=False) \
-	            * unbase_scale * partial_scale
+	        ptsor = (partial_token_sort_ratio(p1, p2, full_process=False) - unbase_scale) * partial_scale
	        ptser = partial_token_set_ratio(p1, p2, full_process=False) \
	            * unbase_scale * partial_scale
	

```
### testWithScorer_amp
  
Lines 199:205

```diff
	        p1 = s1
	        p2 = s2
	
-	    if not utils.validate_string(p1):
+	    if True:
	        return 0
	    if not utils.validate_string(p2):
	        return 0

```  
Lines 201:207

```diff
	
	    if not utils.validate_string(p1):
	        return 0
-	    if not utils.validate_string(p2):
+	    if True:
	        return 0
	
	    return ratio(p1, p2)

```
### testGetBestChoice1_str_emp_0_none_1_str_chr_0
  
Lines 54:60

```diff
	    #   best score === ratio("abcd", "Xbcd")
	    scores = []
	    for block in blocks:
-	        long_start = block[1] - block[0] if (block[1] - block[0]) > 0 else 0
+	        long_start = block[1] - block[0] if ((block[1] * block[0])) > 0 else 0
	        long_end = long_start + len(shorter)
	        long_substr = longer[long_start:long_end]
	

```  
Lines 54:60

```diff
	    #   best score === ratio("abcd", "Xbcd")
	    scores = []
	    for block in blocks:
-	        long_start = block[1] - block[0] if (block[1] - block[0]) > 0 else 0
+	        long_start = (block[1] * block[0]) if (block[1] - block[0]) > 0 else 0
	        long_end = long_start + len(shorter)
	        long_substr = longer[long_start:long_end]
	

```  
Lines 54:60

```diff
	    #   best score === ratio("abcd", "Xbcd")
	    scores = []
	    for block in blocks:
-	        long_start = block[1] - block[0] if (block[1] - block[0]) > 0 else 0
+	        long_start = (block[1] ** block[0]) if (block[1] - block[0]) > 0 else 0
	        long_end = long_start + len(shorter)
	        long_substr = longer[long_start:long_end]
	

```  
Lines 281:287

```diff
	        try_partial = False
	
	    # if one string is much much shorter than the other
-	    if len_ratio > 8:
+	    if False:
	        partial_scale = .6
	
	    if try_partial:

```  
Lines 281:287

```diff
	        try_partial = False
	
	    # if one string is much much shorter than the other
-	    if len_ratio > 8:
+	    if (len_ratio == 8):
	        partial_scale = .6
	
	    if try_partial:

```
### testGetBestChoice3_numb_sub_0_none_2_str_hlf_0
  
Lines 54:60

```diff
	    #   best score === ratio("abcd", "Xbcd")
	    scores = []
	    for block in blocks:
-	        long_start = block[1] - block[0] if (block[1] - block[0]) > 0 else 0
+	        long_start = block[1] - block[0] if ((block[1] + block[0])) > 0 else 0
	        long_end = long_start + len(shorter)
	        long_substr = longer[long_start:long_end]
	

```  
Lines 54:60

```diff
	    #   best score === ratio("abcd", "Xbcd")
	    scores = []
	    for block in blocks:
-	        long_start = block[1] - block[0] if (block[1] - block[0]) > 0 else 0
+	        long_start = block[1] - block[0] if (block[1] - block[0] != 0) else 0
	        long_end = long_start + len(shorter)
	        long_substr = longer[long_start:long_end]
	

```
### testGetBestChoice1_str_hlf_0_none_1
  
Lines 285:291

```diff
	        partial_scale = .6
	
	    if try_partial:
-	        partial = partial_ratio(p1, p2) * partial_scale
+	        partial = (partial_ratio(p1, p2) // partial_scale)
	        ptsor = partial_token_sort_ratio(p1, p2, full_process=False) \
	            * unbase_scale * partial_scale
	        ptser = partial_token_set_ratio(p1, p2, full_process=False) \

```  
Lines 285:291

```diff
	        partial_scale = .6
	
	    if try_partial:
-	        partial = partial_ratio(p1, p2) * partial_scale
+	        partial = (partial_ratio(p1, p2) / partial_scale)
	        ptsor = partial_token_sort_ratio(p1, p2, full_process=False) \
	            * unbase_scale * partial_scale
	        ptser = partial_token_set_ratio(p1, p2, full_process=False) \

```
### testWithCutoff_str_hlf_0_str_hlf_1_str_hlf_4
  
Lines 277:283

```diff
	    len_ratio = float(max(len(p1), len(p2))) / min(len(p1), len(p2))
	
	    # if strings are similar length, don't use partials
-	    if len_ratio < 1.5:
+	    if (len_ratio <= 1.5):
	        try_partial = False
	
	    # if one string is much much shorter than the other

```
### testGetBestChoice1_none_1_str_hlf_0
  
Lines 274:280

```diff
	    partial_scale = .90
	
	    base = ratio(p1, p2)
-	    len_ratio = float(max(len(p1), len(p2))) / min(len(p1), len(p2))
+	    len_ratio = (float(max(len(p1), len(p2))) // min(len(p1), len(p2)))
	
	    # if strings are similar length, don't use partials
	    if len_ratio < 1.5:

```
### test_dedupe_str_emp_8_none_3
  
Lines 127:133

```diff
	    p1 = utils.full_process(s1, force_ascii=force_ascii) if full_process else s1
	    p2 = utils.full_process(s2, force_ascii=force_ascii) if full_process else s2
	
-	    if not utils.validate_string(p1):
+	    if False:
	        return 0
	    if not utils.validate_string(p2):
	        return 0

```
### testNullStrings_str_dbl_0_str_dbl_0_str_dbl_0
  
Lines 281:287

```diff
	        try_partial = False
	
	    # if one string is much much shorter than the other
-	    if len_ratio > 8:
+	    if (len_ratio >= 8):
	        partial_scale = .6
	
	    if try_partial:

```
### testGetBestChoice1_numb_add_0_str_hlf_0_str_hlf_0
  
Lines 54:60

```diff
	    #   best score === ratio("abcd", "Xbcd")
	    scores = []
	    for block in blocks:
-	        long_start = block[1] - block[0] if (block[1] - block[0]) > 0 else 0
+	        long_start = block[1] - block[0] if (block[1] - block[<_ast.Constant object at 0x7f3fd2818a90>]) > 0 else 0
	        long_end = long_start + len(shorter)
	        long_substr = longer[long_start:long_end]
	

```
### test_dedupe_none_10_str_emp_1
  
Lines 121:127

```diff
	        - take ratios of those two strings
	        - controls for unordered partial matches"""
	
-	    if not full_process and s1 == s2:
+	    if False:
	        return 100
	
	    p1 = utils.full_process(s1, force_ascii=force_ascii) if full_process else s1

```
### testWithProcessor_none_12_none_17_str_dbl_4
  
Lines 92:98

```diff
	    sorted1 = _process_and_sort(s1, force_ascii, full_process=full_process)
	    sorted2 = _process_and_sort(s2, force_ascii, full_process=full_process)
	
-	    if partial:
+	    if False:
	        return partial_ratio(sorted1, sorted2)
	    else:
	        return ratio(sorted1, sorted2)

```  
Lines 109:115

```diff
	    """Return the ratio of the most similar substring as a number between
	    0 and 100 but sorting the token before comparing.
	    """
-	    return _token_sort(s1, s2, partial=True, force_ascii=force_ascii, full_process=full_process)
+	    return _token_sort(s1, s2, partial=(False), force_ascii=force_ascii, full_process=full_process)
	
	
	@utils.check_for_none

```  
Lines 109:115

```diff
	    """Return the ratio of the most similar substring as a number between
	    0 and 100 but sorting the token before comparing.
	    """
-	    return _token_sort(s1, s2, partial=True, force_ascii=force_ascii, full_process=full_process)
+	    return _token_sort(s1, s2, partial=None, force_ascii=force_ascii, full_process=full_process)
	
	
	@utils.check_for_none

```  
Lines 286:293

```diff
	
	    if try_partial:
	        partial = partial_ratio(p1, p2) * partial_scale
-	        ptsor = partial_token_sort_ratio(p1, p2, full_process=False) \
-	            * unbase_scale * partial_scale
+	        ptsor = (partial_token_sort_ratio(p1, p2, full_process=False) * unbase_scale %
    partial_scale)
	        ptser = partial_token_set_ratio(p1, p2, full_process=False) \
	            * unbase_scale * partial_scale
	

```  
Lines 286:293

```diff
	
	    if try_partial:
	        partial = partial_ratio(p1, p2) * partial_scale
-	        ptsor = partial_token_sort_ratio(p1, p2, full_process=False) \
-	            * unbase_scale * partial_scale
+	        ptsor = ((partial_token_sort_ratio(p1, p2, full_process=False) * unbase_scale) **
    partial_scale)
	        ptser = partial_token_set_ratio(p1, p2, full_process=False) \
	            * unbase_scale * partial_scale
	

```  
Lines 286:293

```diff
	
	    if try_partial:
	        partial = partial_ratio(p1, p2) * partial_scale
-	        ptsor = partial_token_sort_ratio(p1, p2, full_process=False) \
-	            * unbase_scale * partial_scale
+	        ptsor = (partial_token_sort_ratio(p1, p2, full_process=False) % unbase_scale) * partial_scale
	        ptser = partial_token_set_ratio(p1, p2, full_process=False) \
	            * unbase_scale * partial_scale
	

```  
Lines 286:293

```diff
	
	    if try_partial:
	        partial = partial_ratio(p1, p2) * partial_scale
-	        ptsor = partial_token_sort_ratio(p1, p2, full_process=False) \
-	            * unbase_scale * partial_scale
+	        ptsor = (partial_token_sort_ratio(p1, p2, full_process=False) ** unbase_scale) * partial_scale
	        ptser = partial_token_set_ratio(p1, p2, full_process=False) \
	            * unbase_scale * partial_scale
	

```
### testGetBestChoice2_str_dbl_0_str_hlf_0
  
Lines 92:98

```diff
	    sorted1 = _process_and_sort(s1, force_ascii, full_process=full_process)
	    sorted2 = _process_and_sort(s2, force_ascii, full_process=full_process)
	
-	    if partial:
+	    if True:
	        return partial_ratio(sorted1, sorted2)
	    else:
	        return ratio(sorted1, sorted2)

```  
Lines 102:108

```diff
	    """Return a measure of the sequences' similarity between 0 and 100
	    but sorting the token before comparing.
	    """
-	    return _token_sort(s1, s2, partial=False, force_ascii=force_ascii, full_process=full_process)
+	    return _token_sort(s1, s2, partial=(True), force_ascii=force_ascii, full_process=full_process)
	
	
	def partial_token_sort_ratio(s1, s2, force_ascii=True, full_process=True):

```  
Lines 293:299

```diff
	
	        return utils.intr(max(base, partial, ptsor, ptser))
	    else:
-	        tsor = token_sort_ratio(p1, p2, full_process=False) * unbase_scale
+	        tsor = (token_sort_ratio(p1, p2, full_process=False) - unbase_scale)
	        tser = token_set_ratio(p1, p2, full_process=False) * unbase_scale
	
	        return utils.intr(max(base, tsor, tser))

```  
Lines 293:299

```diff
	
	        return utils.intr(max(base, partial, ptsor, ptser))
	    else:
-	        tsor = token_sort_ratio(p1, p2, full_process=False) * unbase_scale
+	        tsor = (token_sort_ratio(p1, p2, full_process=False) + unbase_scale)
	        tser = token_set_ratio(p1, p2, full_process=False) * unbase_scale
	
	        return utils.intr(max(base, tsor, tser))

```
### testGetBestChoice2_amp
  
Lines 293:299

```diff
	
	        return utils.intr(max(base, partial, ptsor, ptser))
	    else:
-	        tsor = token_sort_ratio(p1, p2, full_process=False) * unbase_scale
+	        tsor = (token_sort_ratio(p1, p2, full_process=False) // unbase_scale)
	        tser = token_set_ratio(p1, p2, full_process=False) * unbase_scale
	
	        return utils.intr(max(base, tsor, tser))

```  
Lines 293:299

```diff
	
	        return utils.intr(max(base, partial, ptsor, ptser))
	    else:
-	        tsor = token_sort_ratio(p1, p2, full_process=False) * unbase_scale
+	        tsor = (token_sort_ratio(p1, p2, full_process=False) / unbase_scale)
	        tser = token_set_ratio(p1, p2, full_process=False) * unbase_scale
	
	        return utils.intr(max(base, tsor, tser))

```
### testNullStrings_none_0_str_hlf_1_str_dbl_1
  
Lines 293:299

```diff
	
	        return utils.intr(max(base, partial, ptsor, ptser))
	    else:
-	        tsor = token_sort_ratio(p1, p2, full_process=False) * unbase_scale
+	        tsor = (token_sort_ratio(p1, p2, full_process=False) % unbase_scale)
	        tser = token_set_ratio(p1, p2, full_process=False) * unbase_scale
	
	        return utils.intr(max(base, tsor, tser))

```  
Lines 293:299

```diff
	
	        return utils.intr(max(base, partial, ptsor, ptser))
	    else:
-	        tsor = token_sort_ratio(p1, p2, full_process=False) * unbase_scale
+	        tsor = (token_sort_ratio(p1, p2, full_process=False) ** unbase_scale)
	        tser = token_set_ratio(p1, p2, full_process=False) * unbase_scale
	
	        return utils.intr(max(base, tsor, tser))

```
### testGetBestChoice1_none_1_str_emp_0
  
Lines 263:269

```diff
	        p1 = s1
	        p2 = s2
	
-	    if not utils.validate_string(p1):
+	    if False:
	        return 0
	    if not utils.validate_string(p2):
	        return 0

```
### testGetBestChoice1_str_hlf_0_none_1_str_dbl_0
  
Lines 294:300

```diff
	        return utils.intr(max(base, partial, ptsor, ptser))
	    else:
	        tsor = token_sort_ratio(p1, p2, full_process=False) * unbase_scale
-	        tser = token_set_ratio(p1, p2, full_process=False) * unbase_scale
+	        tser = (token_set_ratio(p1, p2, full_process=False) // unbase_scale)
	
	        return utils.intr(max(base, tsor, tser))
	

```  
Lines 294:300

```diff
	        return utils.intr(max(base, partial, ptsor, ptser))
	    else:
	        tsor = token_sort_ratio(p1, p2, full_process=False) * unbase_scale
-	        tser = token_set_ratio(p1, p2, full_process=False) * unbase_scale
+	        tser = (token_set_ratio(p1, p2, full_process=False) % unbase_scale)
	
	        return utils.intr(max(base, tsor, tser))
	

```  
Lines 294:300

```diff
	        return utils.intr(max(base, partial, ptsor, ptser))
	    else:
	        tsor = token_sort_ratio(p1, p2, full_process=False) * unbase_scale
-	        tser = token_set_ratio(p1, p2, full_process=False) * unbase_scale
+	        tser = (token_set_ratio(p1, p2, full_process=False) - unbase_scale)
	
	        return utils.intr(max(base, tsor, tser))
	

```  
Lines 294:300

```diff
	        return utils.intr(max(base, partial, ptsor, ptser))
	    else:
	        tsor = token_sort_ratio(p1, p2, full_process=False) * unbase_scale
-	        tser = token_set_ratio(p1, p2, full_process=False) * unbase_scale
+	        tser = (token_set_ratio(p1, p2, full_process=False) / unbase_scale)
	
	        return utils.intr(max(base, tsor, tser))
	

```  
Lines 294:300

```diff
	        return utils.intr(max(base, partial, ptsor, ptser))
	    else:
	        tsor = token_sort_ratio(p1, p2, full_process=False) * unbase_scale
-	        tser = token_set_ratio(p1, p2, full_process=False) * unbase_scale
+	        tser = (token_set_ratio(p1, p2, full_process=False) + unbase_scale)
	
	        return utils.intr(max(base, tsor, tser))
	

```  
Lines 294:300

```diff
	        return utils.intr(max(base, partial, ptsor, ptser))
	    else:
	        tsor = token_sort_ratio(p1, p2, full_process=False) * unbase_scale
-	        tser = token_set_ratio(p1, p2, full_process=False) * unbase_scale
+	        tser = (token_set_ratio(p1, p2, full_process=False) ** unbase_scale)
	
	        return utils.intr(max(base, tsor, tser))
	

```
## Alive Mutants
  
Lines 7:13

```diff
	try:
	    from .StringMatcher import StringMatcher as SequenceMatcher
	except ImportError:
-	    if platform.python_implementation() != "PyPy":
+	    if (platform.python_implementation() < 'PyPy'):
	        warnings.warn('Using slow pure-python SequenceMatcher. Install python-Levenshtein to remove this warning')
	    from difflib import SequenceMatcher
	

```  
Lines 7:13

```diff
	try:
	    from .StringMatcher import StringMatcher as SequenceMatcher
	except ImportError:
-	    if platform.python_implementation() != "PyPy":
+	    if (platform.python_implementation() >= 'PyPy'):
	        warnings.warn('Using slow pure-python SequenceMatcher. Install python-Levenshtein to remove this warning')
	    from difflib import SequenceMatcher
	

```  
Lines 7:13

```diff
	try:
	    from .StringMatcher import StringMatcher as SequenceMatcher
	except ImportError:
-	    if platform.python_implementation() != "PyPy":
+	    if (platform.python_implementation() > 'PyPy'):
	        warnings.warn('Using slow pure-python SequenceMatcher. Install python-Levenshtein to remove this warning')
	    from difflib import SequenceMatcher
	

```  
Lines 7:13

```diff
	try:
	    from .StringMatcher import StringMatcher as SequenceMatcher
	except ImportError:
-	    if platform.python_implementation() != "PyPy":
+	    if (platform.python_implementation() == 'PyPy'):
	        warnings.warn('Using slow pure-python SequenceMatcher. Install python-Levenshtein to remove this warning')
	    from difflib import SequenceMatcher
	

```  
Lines 7:13

```diff
	try:
	    from .StringMatcher import StringMatcher as SequenceMatcher
	except ImportError:
-	    if platform.python_implementation() != "PyPy":
+	    if (platform.python_implementation() <= 'PyPy'):
	        warnings.warn('Using slow pure-python SequenceMatcher. Install python-Levenshtein to remove this warning')
	    from difflib import SequenceMatcher
	

```  
Lines 7:13

```diff
	try:
	    from .StringMatcher import StringMatcher as SequenceMatcher
	except ImportError:
-	    if platform.python_implementation() != "PyPy":
+	    if False:
	        warnings.warn('Using slow pure-python SequenceMatcher. Install python-Levenshtein to remove this warning')
	    from difflib import SequenceMatcher
	

```  
Lines 7:13

```diff
	try:
	    from .StringMatcher import StringMatcher as SequenceMatcher
	except ImportError:
-	    if platform.python_implementation() != "PyPy":
+	    if True:
	        warnings.warn('Using slow pure-python SequenceMatcher. Install python-Levenshtein to remove this warning')
	    from difflib import SequenceMatcher
	

```  
Lines 24:30

```diff
	def ratio(s1, s2):
	    s1, s2 = utils.make_type_consistent(s1, s2)
	
-	    m = SequenceMatcher(None, s1, s2)
+	    m = SequenceMatcher((False), s1, s2)
	    return utils.intr(100 * m.ratio())
	
	

```  
Lines 36:42

```diff
	    as a number between 0 and 100."""
	    s1, s2 = utils.make_type_consistent(s1, s2)
	
-	    if len(s1) <= len(s2):
+	    if (len(s1) < len(s2)):
	        shorter = s1
	        longer = s2
	    else:

```  
Lines 43:49

```diff
	        shorter = s2
	        longer = s1
	
-	    m = SequenceMatcher(None, shorter, longer)
+	    m = SequenceMatcher((False), shorter, longer)
	    blocks = m.get_matching_blocks()
	
	    # each block represents a sequence of matching characters in a string

```  
Lines 54:60

```diff
	    #   best score === ratio("abcd", "Xbcd")
	    scores = []
	    for block in blocks:
-	        long_start = block[1] - block[0] if (block[1] - block[0]) > 0 else 0
+	        long_start = block[1] - block[0] if ((block[1] ** block[0])) > 0 else 0
	        long_end = long_start + len(shorter)
	        long_substr = longer[long_start:long_end]
	

```  
Lines 54:60

```diff
	    #   best score === ratio("abcd", "Xbcd")
	    scores = []
	    for block in blocks:
-	        long_start = block[1] - block[0] if (block[1] - block[0]) > 0 else 0
+	        long_start = block[1] - block[0] if (block[1] - block[0] >= 0) else 0
	        long_end = long_start + len(shorter)
	        long_substr = longer[long_start:long_end]
	

```  
Lines 58:64

```diff
	        long_end = long_start + len(shorter)
	        long_substr = longer[long_start:long_end]
	
-	        m2 = SequenceMatcher(None, shorter, long_substr)
+	        m2 = SequenceMatcher((False), shorter, long_substr)
	        r = m2.ratio()
	        if r > .995:
	            return 100

```  
Lines 60:66

```diff
	
	        m2 = SequenceMatcher(None, shorter, long_substr)
	        r = m2.ratio()
-	        if r > .995:
+	        if (r >= 0.995):
	            return 100
	        else:
	            scores.append(r)

```  
Lines 60:66

```diff
	
	        m2 = SequenceMatcher(None, shorter, long_substr)
	        r = m2.ratio()
-	        if r > .995:
+	        if (r == 0.995):
	            return 100
	        else:
	            scores.append(r)

```  
Lines 60:66

```diff
	
	        m2 = SequenceMatcher(None, shorter, long_substr)
	        r = m2.ratio()
-	        if r > .995:
+	        if False:
	            return 100
	        else:
	            scores.append(r)

```  
Lines 72:78

```diff
	# Advanced Scoring Functions #
	##############################
	
-	def _process_and_sort(s, force_ascii, full_process=True):
+	def _process_and_sort(s, force_ascii, full_process=(False)):
	    """Return a cleaned string with token sorted."""
	    # pull tokens
	    ts = utils.full_process(s, force_ascii=force_ascii) if full_process else s

```  
Lines 72:78

```diff
	# Advanced Scoring Functions #
	##############################
	
-	def _process_and_sort(s, force_ascii, full_process=True):
+	def _process_and_sort(s, force_ascii, full_process=None):
	    """Return a cleaned string with token sorted."""
	    # pull tokens
	    ts = utils.full_process(s, force_ascii=force_ascii) if full_process else s

```  
Lines 88:94

```diff
	#   sort those tokens and take ratio of resulting joined strings
	#   controls for unordered string elements
	@utils.check_for_none
-	def _token_sort(s1, s2, partial=True, force_ascii=True, full_process=True):
+	def _token_sort(s1, s2, partial=(False), force_ascii=True, full_process=True):
	    sorted1 = _process_and_sort(s1, force_ascii, full_process=full_process)
	    sorted2 = _process_and_sort(s2, force_ascii, full_process=full_process)
	

```  
Lines 88:94

```diff
	#   sort those tokens and take ratio of resulting joined strings
	#   controls for unordered string elements
	@utils.check_for_none
-	def _token_sort(s1, s2, partial=True, force_ascii=True, full_process=True):
+	def _token_sort(s1, s2, partial=None, force_ascii=True, full_process=True):
	    sorted1 = _process_and_sort(s1, force_ascii, full_process=full_process)
	    sorted2 = _process_and_sort(s2, force_ascii, full_process=full_process)
	

```  
Lines 88:94

```diff
	#   sort those tokens and take ratio of resulting joined strings
	#   controls for unordered string elements
	@utils.check_for_none
-	def _token_sort(s1, s2, partial=True, force_ascii=True, full_process=True):
+	def _token_sort(s1, s2, partial=True, force_ascii=(False), full_process=True):
	    sorted1 = _process_and_sort(s1, force_ascii, full_process=full_process)
	    sorted2 = _process_and_sort(s2, force_ascii, full_process=full_process)
	

```  
Lines 88:94

```diff
	#   sort those tokens and take ratio of resulting joined strings
	#   controls for unordered string elements
	@utils.check_for_none
-	def _token_sort(s1, s2, partial=True, force_ascii=True, full_process=True):
+	def _token_sort(s1, s2, partial=True, force_ascii=None, full_process=True):
	    sorted1 = _process_and_sort(s1, force_ascii, full_process=full_process)
	    sorted2 = _process_and_sort(s2, force_ascii, full_process=full_process)
	

```  
Lines 88:94

```diff
	#   sort those tokens and take ratio of resulting joined strings
	#   controls for unordered string elements
	@utils.check_for_none
-	def _token_sort(s1, s2, partial=True, force_ascii=True, full_process=True):
+	def _token_sort(s1, s2, partial=True, force_ascii=True, full_process=(False)):
	    sorted1 = _process_and_sort(s1, force_ascii, full_process=full_process)
	    sorted2 = _process_and_sort(s2, force_ascii, full_process=full_process)
	

```  
Lines 88:94

```diff
	#   sort those tokens and take ratio of resulting joined strings
	#   controls for unordered string elements
	@utils.check_for_none
-	def _token_sort(s1, s2, partial=True, force_ascii=True, full_process=True):
+	def _token_sort(s1, s2, partial=True, force_ascii=True, full_process=None):
	    sorted1 = _process_and_sort(s1, force_ascii, full_process=full_process)
	    sorted2 = _process_and_sort(s2, force_ascii, full_process=full_process)
	

```  
Lines 98:104

```diff
	        return ratio(sorted1, sorted2)
	
	
-	def token_sort_ratio(s1, s2, force_ascii=True, full_process=True):
+	def token_sort_ratio(s1, s2, force_ascii=(False), full_process=True):
	    """Return a measure of the sequences' similarity between 0 and 100
	    but sorting the token before comparing.
	    """

```  
Lines 98:104

```diff
	        return ratio(sorted1, sorted2)
	
	
-	def token_sort_ratio(s1, s2, force_ascii=True, full_process=True):
+	def token_sort_ratio(s1, s2, force_ascii=None, full_process=True):
	    """Return a measure of the sequences' similarity between 0 and 100
	    but sorting the token before comparing.
	    """

```  
Lines 98:104

```diff
	        return ratio(sorted1, sorted2)
	
	
-	def token_sort_ratio(s1, s2, force_ascii=True, full_process=True):
+	def token_sort_ratio(s1, s2, force_ascii=True, full_process=(False)):
	    """Return a measure of the sequences' similarity between 0 and 100
	    but sorting the token before comparing.
	    """

```  
Lines 98:104

```diff
	        return ratio(sorted1, sorted2)
	
	
-	def token_sort_ratio(s1, s2, force_ascii=True, full_process=True):
+	def token_sort_ratio(s1, s2, force_ascii=True, full_process=None):
	    """Return a measure of the sequences' similarity between 0 and 100
	    but sorting the token before comparing.
	    """

```  
Lines 102:108

```diff
	    """Return a measure of the sequences' similarity between 0 and 100
	    but sorting the token before comparing.
	    """
-	    return _token_sort(s1, s2, partial=False, force_ascii=force_ascii, full_process=full_process)
+	    return _token_sort(s1, s2, partial=None, force_ascii=force_ascii, full_process=full_process)
	
	
	def partial_token_sort_ratio(s1, s2, force_ascii=True, full_process=True):

```  
Lines 105:111

```diff
	    return _token_sort(s1, s2, partial=False, force_ascii=force_ascii, full_process=full_process)
	
	
-	def partial_token_sort_ratio(s1, s2, force_ascii=True, full_process=True):
+	def partial_token_sort_ratio(s1, s2, force_ascii=(False), full_process=True):
	    """Return the ratio of the most similar substring as a number between
	    0 and 100 but sorting the token before comparing.
	    """

```  
Lines 105:111

```diff
	    return _token_sort(s1, s2, partial=False, force_ascii=force_ascii, full_process=full_process)
	
	
-	def partial_token_sort_ratio(s1, s2, force_ascii=True, full_process=True):
+	def partial_token_sort_ratio(s1, s2, force_ascii=None, full_process=True):
	    """Return the ratio of the most similar substring as a number between
	    0 and 100 but sorting the token before comparing.
	    """

```  
Lines 105:111

```diff
	    return _token_sort(s1, s2, partial=False, force_ascii=force_ascii, full_process=full_process)
	
	
-	def partial_token_sort_ratio(s1, s2, force_ascii=True, full_process=True):
+	def partial_token_sort_ratio(s1, s2, force_ascii=True, full_process=(False)):
	    """Return the ratio of the most similar substring as a number between
	    0 and 100 but sorting the token before comparing.
	    """

```  
Lines 105:111

```diff
	    return _token_sort(s1, s2, partial=False, force_ascii=force_ascii, full_process=full_process)
	
	
-	def partial_token_sort_ratio(s1, s2, force_ascii=True, full_process=True):
+	def partial_token_sort_ratio(s1, s2, force_ascii=True, full_process=None):
	    """Return the ratio of the most similar substring as a number between
	    0 and 100 but sorting the token before comparing.
	    """

```  
Lines 113:119

```diff
	
	
	@utils.check_for_none
-	def _token_set(s1, s2, partial=True, force_ascii=True, full_process=True):
+	def _token_set(s1, s2, partial=True, force_ascii=(False), full_process=True):
	    """Find all alphanumeric tokens in each string...
	        - treat them as a set
	        - construct two strings of the form:

```  
Lines 113:119

```diff
	
	
	@utils.check_for_none
-	def _token_set(s1, s2, partial=True, force_ascii=True, full_process=True):
+	def _token_set(s1, s2, partial=True, force_ascii=None, full_process=True):
	    """Find all alphanumeric tokens in each string...
	        - treat them as a set
	        - construct two strings of the form:

```  
Lines 113:119

```diff
	
	
	@utils.check_for_none
-	def _token_set(s1, s2, partial=True, force_ascii=True, full_process=True):
+	def _token_set(s1, s2, partial=True, force_ascii=True, full_process=(False)):
	    """Find all alphanumeric tokens in each string...
	        - treat them as a set
	        - construct two strings of the form:

```  
Lines 113:119

```diff
	
	
	@utils.check_for_none
-	def _token_set(s1, s2, partial=True, force_ascii=True, full_process=True):
+	def _token_set(s1, s2, partial=True, force_ascii=True, full_process=None):
	    """Find all alphanumeric tokens in each string...
	        - treat them as a set
	        - construct two strings of the form:

```  
Lines 113:119

```diff
	
	
	@utils.check_for_none
-	def _token_set(s1, s2, partial=True, force_ascii=True, full_process=True):
+	def _token_set(s1, s2, partial=(False), force_ascii=True, full_process=True):
	    """Find all alphanumeric tokens in each string...
	        - treat them as a set
	        - construct two strings of the form:

```  
Lines 113:119

```diff
	
	
	@utils.check_for_none
-	def _token_set(s1, s2, partial=True, force_ascii=True, full_process=True):
+	def _token_set(s1, s2, partial=None, force_ascii=True, full_process=True):
	    """Find all alphanumeric tokens in each string...
	        - treat them as a set
	        - construct two strings of the form:

```  
Lines 129:135

```diff
	
	    if not utils.validate_string(p1):
	        return 0
-	    if not utils.validate_string(p2):
+	    if False:
	        return 0
	
	    # pull tokens

```  
Lines 165:171

```diff
	    return max(pairwise)
	
	
-	def token_set_ratio(s1, s2, force_ascii=True, full_process=True):
+	def token_set_ratio(s1, s2, force_ascii=True, full_process=(False)):
	    return _token_set(s1, s2, partial=False, force_ascii=force_ascii, full_process=full_process)
	
	

```  
Lines 165:171

```diff
	    return max(pairwise)
	
	
-	def token_set_ratio(s1, s2, force_ascii=True, full_process=True):
+	def token_set_ratio(s1, s2, force_ascii=True, full_process=None):
	    return _token_set(s1, s2, partial=False, force_ascii=force_ascii, full_process=full_process)
	
	

```  
Lines 165:171

```diff
	    return max(pairwise)
	
	
-	def token_set_ratio(s1, s2, force_ascii=True, full_process=True):
+	def token_set_ratio(s1, s2, force_ascii=(False), full_process=True):
	    return _token_set(s1, s2, partial=False, force_ascii=force_ascii, full_process=full_process)
	
	

```  
Lines 165:171

```diff
	    return max(pairwise)
	
	
-	def token_set_ratio(s1, s2, force_ascii=True, full_process=True):
+	def token_set_ratio(s1, s2, force_ascii=None, full_process=True):
	    return _token_set(s1, s2, partial=False, force_ascii=force_ascii, full_process=full_process)
	
	

```  
Lines 166:172

```diff
	
	
	def token_set_ratio(s1, s2, force_ascii=True, full_process=True):
-	    return _token_set(s1, s2, partial=False, force_ascii=force_ascii, full_process=full_process)
+	    return _token_set(s1, s2, partial=None, force_ascii=force_ascii, full_process=full_process)
	
	
	def partial_token_set_ratio(s1, s2, force_ascii=True, full_process=True):

```  
Lines 169:175

```diff
	    return _token_set(s1, s2, partial=False, force_ascii=force_ascii, full_process=full_process)
	
	
-	def partial_token_set_ratio(s1, s2, force_ascii=True, full_process=True):
+	def partial_token_set_ratio(s1, s2, force_ascii=True, full_process=(False)):
	    return _token_set(s1, s2, partial=True, force_ascii=force_ascii, full_process=full_process)
	
	

```  
Lines 169:175

```diff
	    return _token_set(s1, s2, partial=False, force_ascii=force_ascii, full_process=full_process)
	
	
-	def partial_token_set_ratio(s1, s2, force_ascii=True, full_process=True):
+	def partial_token_set_ratio(s1, s2, force_ascii=True, full_process=None):
	    return _token_set(s1, s2, partial=True, force_ascii=force_ascii, full_process=full_process)
	
	

```  
Lines 169:175

```diff
	    return _token_set(s1, s2, partial=False, force_ascii=force_ascii, full_process=full_process)
	
	
-	def partial_token_set_ratio(s1, s2, force_ascii=True, full_process=True):
+	def partial_token_set_ratio(s1, s2, force_ascii=(False), full_process=True):
	    return _token_set(s1, s2, partial=True, force_ascii=force_ascii, full_process=full_process)
	
	

```  
Lines 169:175

```diff
	    return _token_set(s1, s2, partial=False, force_ascii=force_ascii, full_process=full_process)
	
	
-	def partial_token_set_ratio(s1, s2, force_ascii=True, full_process=True):
+	def partial_token_set_ratio(s1, s2, force_ascii=None, full_process=True):
	    return _token_set(s1, s2, partial=True, force_ascii=force_ascii, full_process=full_process)
	
	

```  
Lines 178:184

```diff
	###################
	
	# q is for quick
-	def QRatio(s1, s2, force_ascii=True, full_process=True):
+	def QRatio(s1, s2, force_ascii=True, full_process=(False)):
	    """
	    Quick ratio comparison between two strings.
	

```  
Lines 178:184

```diff
	###################
	
	# q is for quick
-	def QRatio(s1, s2, force_ascii=True, full_process=True):
+	def QRatio(s1, s2, force_ascii=True, full_process=None):
	    """
	    Quick ratio comparison between two strings.
	

```  
Lines 178:184

```diff
	###################
	
	# q is for quick
-	def QRatio(s1, s2, force_ascii=True, full_process=True):
+	def QRatio(s1, s2, force_ascii=(False), full_process=True):
	    """
	    Quick ratio comparison between two strings.
	

```  
Lines 178:184

```diff
	###################
	
	# q is for quick
-	def QRatio(s1, s2, force_ascii=True, full_process=True):
+	def QRatio(s1, s2, force_ascii=None, full_process=True):
	    """
	    Quick ratio comparison between two strings.
	

```  
Lines 192:198

```diff
	    :return: similarity ratio
	    """
	
-	    if full_process:
+	    if False:
	        p1 = utils.full_process(s1, force_ascii=force_ascii)
	        p2 = utils.full_process(s2, force_ascii=force_ascii)
	    else:

```  
Lines 192:198

```diff
	    :return: similarity ratio
	    """
	
-	    if full_process:
+	    if True:
	        p1 = utils.full_process(s1, force_ascii=force_ascii)
	        p2 = utils.full_process(s2, force_ascii=force_ascii)
	    else:

```  
Lines 199:205

```diff
	        p1 = s1
	        p2 = s2
	
-	    if not utils.validate_string(p1):
+	    if False:
	        return 0
	    if not utils.validate_string(p2):
	        return 0

```  
Lines 201:207

```diff
	
	    if not utils.validate_string(p1):
	        return 0
-	    if not utils.validate_string(p2):
+	    if False:
	        return 0
	
	    return ratio(p1, p2)

```  
Lines 207:213

```diff
	    return ratio(p1, p2)
	
	
-	def UQRatio(s1, s2, full_process=True):
+	def UQRatio(s1, s2, full_process=(False)):
	    """
	    Unicode quick ratio
	

```  
Lines 207:213

```diff
	    return ratio(p1, p2)
	
	
-	def UQRatio(s1, s2, full_process=True):
+	def UQRatio(s1, s2, full_process=None):
	    """
	    Unicode quick ratio
	

```  
Lines 221:227

```diff
	
	
	# w is for weighted
-	def WRatio(s1, s2, force_ascii=True, full_process=True):
+	def WRatio(s1, s2, force_ascii=(False), full_process=True):
	    """
	    Return a measure of the sequences' similarity between 0 and 100, using different algorithms.
	

```  
Lines 221:227

```diff
	
	
	# w is for weighted
-	def WRatio(s1, s2, force_ascii=True, full_process=True):
+	def WRatio(s1, s2, force_ascii=None, full_process=True):
	    """
	    Return a measure of the sequences' similarity between 0 and 100, using different algorithms.
	

```  
Lines 221:227

```diff
	
	
	# w is for weighted
-	def WRatio(s1, s2, force_ascii=True, full_process=True):
+	def WRatio(s1, s2, force_ascii=True, full_process=(False)):
	    """
	    Return a measure of the sequences' similarity between 0 and 100, using different algorithms.
	

```  
Lines 221:227

```diff
	
	
	# w is for weighted
-	def WRatio(s1, s2, force_ascii=True, full_process=True):
+	def WRatio(s1, s2, force_ascii=True, full_process=None):
	    """
	    Return a measure of the sequences' similarity between 0 and 100, using different algorithms.
	

```  
Lines 256:262

```diff
	    :return:
	    """
	
-	    if full_process:
+	    if False:
	        p1 = utils.full_process(s1, force_ascii=force_ascii)
	        p2 = utils.full_process(s2, force_ascii=force_ascii)
	    else:

```  
Lines 256:262

```diff
	    :return:
	    """
	
-	    if full_process:
+	    if True:
	        p1 = utils.full_process(s1, force_ascii=force_ascii)
	        p2 = utils.full_process(s2, force_ascii=force_ascii)
	    else:

```  
Lines 278:284

```diff
	
	    # if strings are similar length, don't use partials
	    if len_ratio < 1.5:
-	        try_partial = False
+	        try_partial = None
	
	    # if one string is much much shorter than the other
	    if len_ratio > 8:

```  
Lines 286:292

```diff
	
	    if try_partial:
	        partial = partial_ratio(p1, p2) * partial_scale
-	        ptsor = partial_token_sort_ratio(p1, p2, full_process=False) \
+	        ptsor = partial_token_sort_ratio(p1, p2, full_process=(True)) \
	            * unbase_scale * partial_scale
	        ptser = partial_token_set_ratio(p1, p2, full_process=False) \
	            * unbase_scale * partial_scale

```  
Lines 286:292

```diff
	
	    if try_partial:
	        partial = partial_ratio(p1, p2) * partial_scale
-	        ptsor = partial_token_sort_ratio(p1, p2, full_process=False) \
+	        ptsor = partial_token_sort_ratio(p1, p2, full_process=None) \
	            * unbase_scale * partial_scale
	        ptser = partial_token_set_ratio(p1, p2, full_process=False) \
	            * unbase_scale * partial_scale

```  
Lines 288:294

```diff
	        partial = partial_ratio(p1, p2) * partial_scale
	        ptsor = partial_token_sort_ratio(p1, p2, full_process=False) \
	            * unbase_scale * partial_scale
-	        ptser = partial_token_set_ratio(p1, p2, full_process=False) \
+	        ptser = partial_token_set_ratio(p1, p2, full_process=(True)) \
	            * unbase_scale * partial_scale
	
	        return utils.intr(max(base, partial, ptsor, ptser))

```  
Lines 288:294

```diff
	        partial = partial_ratio(p1, p2) * partial_scale
	        ptsor = partial_token_sort_ratio(p1, p2, full_process=False) \
	            * unbase_scale * partial_scale
-	        ptser = partial_token_set_ratio(p1, p2, full_process=False) \
+	        ptser = partial_token_set_ratio(p1, p2, full_process=None) \
	            * unbase_scale * partial_scale
	
	        return utils.intr(max(base, partial, ptsor, ptser))

```  
Lines 293:299

```diff
	
	        return utils.intr(max(base, partial, ptsor, ptser))
	    else:
-	        tsor = token_sort_ratio(p1, p2, full_process=False) * unbase_scale
+	        tsor = token_sort_ratio(p1, p2, full_process=(True)) * unbase_scale
	        tser = token_set_ratio(p1, p2, full_process=False) * unbase_scale
	
	        return utils.intr(max(base, tsor, tser))

```  
Lines 293:299

```diff
	
	        return utils.intr(max(base, partial, ptsor, ptser))
	    else:
-	        tsor = token_sort_ratio(p1, p2, full_process=False) * unbase_scale
+	        tsor = token_sort_ratio(p1, p2, full_process=None) * unbase_scale
	        tser = token_set_ratio(p1, p2, full_process=False) * unbase_scale
	
	        return utils.intr(max(base, tsor, tser))

```  
Lines 294:300

```diff
	        return utils.intr(max(base, partial, ptsor, ptser))
	    else:
	        tsor = token_sort_ratio(p1, p2, full_process=False) * unbase_scale
-	        tser = token_set_ratio(p1, p2, full_process=False) * unbase_scale
+	        tser = token_set_ratio(p1, p2, full_process=(True)) * unbase_scale
	
	        return utils.intr(max(base, tsor, tser))
	

```  
Lines 294:300

```diff
	        return utils.intr(max(base, partial, ptsor, ptser))
	    else:
	        tsor = token_sort_ratio(p1, p2, full_process=False) * unbase_scale
-	        tser = token_set_ratio(p1, p2, full_process=False) * unbase_scale
+	        tser = token_set_ratio(p1, p2, full_process=None) * unbase_scale
	
	        return utils.intr(max(base, tsor, tser))
	

```  
Lines 299:306

```diff
	        return utils.intr(max(base, tsor, tser))
	
	
-	def UWRatio(s1, s2, full_process=True):
+	def UWRatio(s1, s2, full_process=(False)):
	    """Return a measure of the sequences' similarity between 0 and 100,
	    using different algorithms. Same as WRatio but preserving unicode.
	    """
	    return WRatio(s1, s2, force_ascii=False, full_process=full_process)

```  
Lines 299:306

```diff
	        return utils.intr(max(base, tsor, tser))
	
	
-	def UWRatio(s1, s2, full_process=True):
+	def UWRatio(s1, s2, full_process=None):
	    """Return a measure of the sequences' similarity between 0 and 100,
	    using different algorithms. Same as WRatio but preserving unicode.
	    """
	    return WRatio(s1, s2, force_ascii=False, full_process=full_process)

```
# /home/ubuntu/projects/thefuzz/thefuzz/utils.py

## Newly Killed Mutants

### testGetBestChoice1_str_hlf_0_none_1_str_dbl_0
  
Lines 5:11

```diff
	from thefuzz.string_processing import StringProcessor
	
	
-	PY3 = sys.version_info[0] == 3
+	PY3 = (sys.version_info[0] >= 3)
	
	
	def validate_string(s):

```  
Lines 5:11

```diff
	from thefuzz.string_processing import StringProcessor
	
	
-	PY3 = sys.version_info[0] == 3
+	PY3 = (sys.version_info[0] <= 3)
	
	
	def validate_string(s):

```  
Lines 16:22

```diff
	    :return: True if len(s) > 0 else False
	    """
	    try:
-	        return len(s) > 0
+	        return (len(s) != 0)
	    except TypeError:
	        return False
	

```  
Lines 24:30

```diff
	def check_for_equivalence(func):
	    @functools.wraps(func)
	    def decorator(*args, **kwargs):
-	        if args[0] == args[1]:
+	        if False:
	            return 100
	        return func(*args, **kwargs)
	    return decorator

```  
Lines 24:30

```diff
	def check_for_equivalence(func):
	    @functools.wraps(func)
	    def decorator(*args, **kwargs):
-	        if args[0] == args[1]:
+	        if args[0] == args[<_ast.Constant object at 0x7f3fc399f070>]:
	            return 100
	        return func(*args, **kwargs)
	    return decorator

```  
Lines 33:39

```diff
	def check_for_none(func):
	    @functools.wraps(func)
	    def decorator(*args, **kwargs):
-	        if args[0] is None or args[1] is None:
+	        if args[0] is (False) or args[1] is None:
	            return 0
	        return func(*args, **kwargs)
	    return decorator

```  
Lines 33:39

```diff
	def check_for_none(func):
	    @functools.wraps(func)
	    def decorator(*args, **kwargs):
-	        if args[0] is None or args[1] is None:
+	        if args[0] is (True) or args[1] is None:
	            return 0
	        return func(*args, **kwargs)
	    return decorator

```  
Lines 33:39

```diff
	def check_for_none(func):
	    @functools.wraps(func)
	    def decorator(*args, **kwargs):
-	        if args[0] is None or args[1] is None:
+	        if False:
	            return 0
	        return func(*args, **kwargs)
	    return decorator

```  
Lines 33:39

```diff
	def check_for_none(func):
	    @functools.wraps(func)
	    def decorator(*args, **kwargs):
-	        if args[0] is None or args[1] is None:
+	        if (args[0] is None and args[1] is None):
	            return 0
	        return func(*args, **kwargs)
	    return decorator

```  
Lines 33:39

```diff
	def check_for_none(func):
	    @functools.wraps(func)
	    def decorator(*args, **kwargs):
-	        if args[0] is None or args[1] is None:
+	        if args[<_ast.Constant object at 0x7f3fc185a6a0>] is None or args[1] is None:
	            return 0
	        return func(*args, **kwargs)
	    return decorator

```  
Lines 33:39

```diff
	def check_for_none(func):
	    @functools.wraps(func)
	    def decorator(*args, **kwargs):
-	        if args[0] is None or args[1] is None:
+	        if args[<_ast.Constant object at 0x7f3fc185a820>] is None or args[1] is None:
	            return 0
	        return func(*args, **kwargs)
	    return decorator

```  
Lines 33:39

```diff
	def check_for_none(func):
	    @functools.wraps(func)
	    def decorator(*args, **kwargs):
-	        if args[0] is None or args[1] is None:
+	        if args[0] is None or args[<_ast.Constant object at 0x7f3fc185a490>] is None:
	            return 0
	        return func(*args, **kwargs)
	    return decorator

```  
Lines 33:39

```diff
	def check_for_none(func):
	    @functools.wraps(func)
	    def decorator(*args, **kwargs):
-	        if args[0] is None or args[1] is None:
+	        if args[0] is None or args[<_ast.Constant object at 0x7f3fc185a820>] is None:
	            return 0
	        return func(*args, **kwargs)
	    return decorator

```  
Lines 33:39

```diff
	def check_for_none(func):
	    @functools.wraps(func)
	    def decorator(*args, **kwargs):
-	        if args[0] is None or args[1] is None:
+	        if args[0] is None or args[1] is (False):
	            return 0
	        return func(*args, **kwargs)
	    return decorator

```  
Lines 33:39

```diff
	def check_for_none(func):
	    @functools.wraps(func)
	    def decorator(*args, **kwargs):
-	        if args[0] is None or args[1] is None:
+	        if args[0] is None or args[1] is (True):
	            return 0
	        return func(*args, **kwargs)
	    return decorator

```  
Lines 42:48

```diff
	def check_empty_string(func):
	    @functools.wraps(func)
	    def decorator(*args, **kwargs):
-	        if len(args[0]) == 0 or len(args[1]) == 0:
+	        if len(args[0]) == 0 or (len(args[1]) < 0):
	            return 0
	        return func(*args, **kwargs)
	    return decorator

```  
Lines 42:48

```diff
	def check_empty_string(func):
	    @functools.wraps(func)
	    def decorator(*args, **kwargs):
-	        if len(args[0]) == 0 or len(args[1]) == 0:
+	        if len(args[0]) == 0 or (len(args[1]) <= 0):
	            return 0
	        return func(*args, **kwargs)
	    return decorator

```  
Lines 42:48

```diff
	def check_empty_string(func):
	    @functools.wraps(func)
	    def decorator(*args, **kwargs):
-	        if len(args[0]) == 0 or len(args[1]) == 0:
+	        if (len(args[0]) <= 0) or len(args[1]) == 0:
	            return 0
	        return func(*args, **kwargs)
	    return decorator

```  
Lines 42:48

```diff
	def check_empty_string(func):
	    @functools.wraps(func)
	    def decorator(*args, **kwargs):
-	        if len(args[0]) == 0 or len(args[1]) == 0:
+	        if len(args[0]) == 0 or len(args[<_ast.Constant object at 0x7f3fc185a6a0>]) == 0:
	            return 0
	        return func(*args, **kwargs)
	    return decorator

```  
Lines 42:48

```diff
	def check_empty_string(func):
	    @functools.wraps(func)
	    def decorator(*args, **kwargs):
-	        if len(args[0]) == 0 or len(args[1]) == 0:
+	        if len(args[0]) == 0 or len(args[<_ast.Constant object at 0x7f3fc185a820>]) == 0:
	            return 0
	        return func(*args, **kwargs)
	    return decorator

```  
Lines 49:55

```diff
	
	
	bad_chars = str("").join([chr(i) for i in range(128, 256)])  # ascii dammit!
-	if PY3:
+	if True:
	    translation_table = dict((ord(c), None) for c in bad_chars)
	    unicode = str
	

```  
Lines 50:56

```diff
	
	bad_chars = str("").join([chr(i) for i in range(128, 256)])  # ascii dammit!
	if PY3:
-	    translation_table = dict((ord(c), None) for c in bad_chars)
+	    translation_table = dict((ord(c), (False)) for c in bad_chars)
	    unicode = str
	
	

```  
Lines 50:56

```diff
	
	bad_chars = str("").join([chr(i) for i in range(128, 256)])  # ascii dammit!
	if PY3:
-	    translation_table = dict((ord(c), None) for c in bad_chars)
+	    translation_table = dict((ord(c), (True)) for c in bad_chars)
	    unicode = str
	
	

```  
Lines 55:61

```diff
	
	
	def asciionly(s):
-	    if PY3:
+	    if True:
	        return s.translate(translation_table)
	    else:
	        return s.translate(None, bad_chars)

```  
Lines 64:70

```diff
	def asciidammit(s):
	    if type(s) is str:
	        return asciionly(s)
-	    elif type(s) is unicode:
+	    elif False:
	        return asciionly(s.encode('ascii', 'ignore'))
	    else:
	        return asciidammit(unicode(s))

```  
Lines 72:78

```diff
	
	def make_type_consistent(s1, s2):
	    """If both objects aren't either both string or unicode instances force them to unicode"""
-	    if isinstance(s1, str) and isinstance(s2, str):
+	    if False:
	        return s1, s2
	
	    elif isinstance(s1, unicode) and isinstance(s2, unicode):

```  
Lines 72:78

```diff
	
	def make_type_consistent(s1, s2):
	    """If both objects aren't either both string or unicode instances force them to unicode"""
-	    if isinstance(s1, str) and isinstance(s2, str):
+	    if True:
	        return s1, s2
	
	    elif isinstance(s1, unicode) and isinstance(s2, unicode):

```  
Lines 72:78

```diff
	
	def make_type_consistent(s1, s2):
	    """If both objects aren't either both string or unicode instances force them to unicode"""
-	    if isinstance(s1, str) and isinstance(s2, str):
+	    if (isinstance(s1, str) or isinstance(s2, str)):
	        return s1, s2
	
	    elif isinstance(s1, unicode) and isinstance(s2, unicode):

```  
Lines 82:88

```diff
	        return unicode(s1), unicode(s2)
	
	
-	def full_process(s, force_ascii=False):
+	def full_process(s, force_ascii=(True)):
	    """Process string by
	        -- removing all but letters and numbers
	        -- trim whitespace

```  
Lines 82:88

```diff
	        return unicode(s1), unicode(s2)
	
	
-	def full_process(s, force_ascii=False):
+	def full_process(s, force_ascii=None):
	    """Process string by
	        -- removing all but letters and numbers
	        -- trim whitespace

```  
Lines 89:95

```diff
	        -- force to lower case
	        if force_ascii == True, force convert to ascii"""
	
-	    if force_ascii:
+	    if True:
	        s = asciidammit(s)
	    # Keep only Letters and Numbers (see Unicode docs).
	    string_out = StringProcessor.replace_non_letters_non_numbers_with_whitespace(s)

```
### testGetBestChoice1_str_hlf_0_none_1
  
Lines 42:48

```diff
	def check_empty_string(func):
	    @functools.wraps(func)
	    def decorator(*args, **kwargs):
-	        if len(args[0]) == 0 or len(args[1]) == 0:
+	        if (len(args[0]) < 0) or len(args[1]) == 0:
	            return 0
	        return func(*args, **kwargs)
	    return decorator

```  
Lines 42:48

```diff
	def check_empty_string(func):
	    @functools.wraps(func)
	    def decorator(*args, **kwargs):
-	        if len(args[0]) == 0 or len(args[1]) == 0:
+	        if (len(args[0]) == 0 and len(args[1]) == 0):
	            return 0
	        return func(*args, **kwargs)
	    return decorator

```  
Lines 42:48

```diff
	def check_empty_string(func):
	    @functools.wraps(func)
	    def decorator(*args, **kwargs):
-	        if len(args[0]) == 0 or len(args[1]) == 0:
+	        if False:
	            return 0
	        return func(*args, **kwargs)
	    return decorator

```  
Lines 42:48

```diff
	def check_empty_string(func):
	    @functools.wraps(func)
	    def decorator(*args, **kwargs):
-	        if len(args[0]) == 0 or len(args[1]) == 0:
+	        if len(args[<_ast.Constant object at 0x7f3fc185aa90>]) == 0 or len(args[1]) == 0:
	            return 0
	        return func(*args, **kwargs)
	    return decorator

```  
Lines 42:48

```diff
	def check_empty_string(func):
	    @functools.wraps(func)
	    def decorator(*args, **kwargs):
-	        if len(args[0]) == 0 or len(args[1]) == 0:
+	        if len(args[<_ast.Constant object at 0x7f3fc185a820>]) == 0 or len(args[1]) == 0:
	            return 0
	        return func(*args, **kwargs)
	    return decorator

```
## Alive Mutants

# /home/ubuntu/projects/thefuzz/thefuzz/string_processing.py

## Newly Killed Mutants

### testGetBestChoice1_str_hlf_0_none_1_str_dbl_0
  
Lines 3:9

```diff
	import string
	import sys
	
-	PY3 = sys.version_info[0] == 3
+	PY3 = (sys.version_info[0] >= 3)
	if PY3:
	    string = str
	

```  
Lines 3:9

```diff
	import string
	import sys
	
-	PY3 = sys.version_info[0] == 3
+	PY3 = (sys.version_info[0] <= 3)
	if PY3:
	    string = str
	

```  
Lines 4:10

```diff
	import sys
	
	PY3 = sys.version_info[0] == 3
-	if PY3:
+	if True:
	    string = str
	
	

```
## Alive Mutants

# /home/ubuntu/projects/thefuzz/thefuzz/StringMatcher.py

## Newly Killed Mutants

## Alive Mutants

# /home/ubuntu/projects/thefuzz/thefuzz/__init__.py

## Newly Killed Mutants

## Alive Mutants

# /home/ubuntu/projects/thefuzz/thefuzz/process.py

## Newly Killed Mutants

## Alive Mutants
