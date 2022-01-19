



# /home/ebert/projects/python-twelve-tone/src/twelve_tone/midi.py

## Newly Killed Mutants

### test_create_amp
  
Lines 14:20

```diff
	        attack = 200
	        beats = 1
	        for note in notes:
-	            pitch = (note - 1) + offset
+	            pitch = ((note // 1)) + offset
	            midinote = [self.step_counter, pitch, attack, beats]
	            midinotes.append(midinote)
	            self.step_counter = self.step_counter + 1

```  
Lines 14:20

```diff
	        attack = 200
	        beats = 1
	        for note in notes:
-	            pitch = (note - 1) + offset
+	            pitch = ((note * 1)) + offset
	            midinote = [self.step_counter, pitch, attack, beats]
	            midinotes.append(midinote)
	            self.step_counter = self.step_counter + 1

```  
Lines 14:20

```diff
	        attack = 200
	        beats = 1
	        for note in notes:
-	            pitch = (note - 1) + offset
+	            pitch = ((note % 1)) + offset
	            midinote = [self.step_counter, pitch, attack, beats]
	            midinotes.append(midinote)
	            self.step_counter = self.step_counter + 1

```  
Lines 14:20

```diff
	        attack = 200
	        beats = 1
	        for note in notes:
-	            pitch = (note - 1) + offset
+	            pitch = ((note + 1)) + offset
	            midinote = [self.step_counter, pitch, attack, beats]
	            midinotes.append(midinote)
	            self.step_counter = self.step_counter + 1

```  
Lines 14:20

```diff
	        attack = 200
	        beats = 1
	        for note in notes:
-	            pitch = (note - 1) + offset
+	            pitch = ((note ** 1)) + offset
	            midinote = [self.step_counter, pitch, attack, beats]
	            midinotes.append(midinote)
	            self.step_counter = self.step_counter + 1

```  
Lines 14:20

```diff
	        attack = 200
	        beats = 1
	        for note in notes:
-	            pitch = (note - 1) + offset
+	            pitch = ((note - 1) // offset)
	            midinote = [self.step_counter, pitch, attack, beats]
	            midinotes.append(midinote)
	            self.step_counter = self.step_counter + 1

```  
Lines 14:20

```diff
	        attack = 200
	        beats = 1
	        for note in notes:
-	            pitch = (note - 1) + offset
+	            pitch = ((note - 1) % offset)
	            midinote = [self.step_counter, pitch, attack, beats]
	            midinotes.append(midinote)
	            self.step_counter = self.step_counter + 1

```  
Lines 17:23

```diff
	            pitch = (note - 1) + offset
	            midinote = [self.step_counter, pitch, attack, beats]
	            midinotes.append(midinote)
-	            self.step_counter = self.step_counter + 1
+	            self.step_counter = (self.step_counter // 1)
	
	        # Add a track with those notes
	        self.pattern.add_track(midinotes)

```  
Lines 17:23

```diff
	            pitch = (note - 1) + offset
	            midinote = [self.step_counter, pitch, attack, beats]
	            midinotes.append(midinote)
-	            self.step_counter = self.step_counter + 1
+	            self.step_counter = (self.step_counter * 1)
	
	        # Add a track with those notes
	        self.pattern.add_track(midinotes)

```  
Lines 17:23

```diff
	            pitch = (note - 1) + offset
	            midinote = [self.step_counter, pitch, attack, beats]
	            midinotes.append(midinote)
-	            self.step_counter = self.step_counter + 1
+	            self.step_counter = (self.step_counter % 1)
	
	        # Add a track with those notes
	        self.pattern.add_track(midinotes)

```  
Lines 17:23

```diff
	            pitch = (note - 1) + offset
	            midinote = [self.step_counter, pitch, attack, beats]
	            midinotes.append(midinote)
-	            self.step_counter = self.step_counter + 1
+	            self.step_counter = (self.step_counter - 1)
	
	        # Add a track with those notes
	        self.pattern.add_track(midinotes)

```  
Lines 17:23

```diff
	            pitch = (note - 1) + offset
	            midinote = [self.step_counter, pitch, attack, beats]
	            midinotes.append(midinote)
-	            self.step_counter = self.step_counter + 1
+	            self.step_counter = (self.step_counter / 1)
	
	        # Add a track with those notes
	        self.pattern.add_track(midinotes)

```  
Lines 17:23

```diff
	            pitch = (note - 1) + offset
	            midinote = [self.step_counter, pitch, attack, beats]
	            midinotes.append(midinote)
-	            self.step_counter = self.step_counter + 1
+	            self.step_counter = (self.step_counter ** 1)
	
	        # Add a track with those notes
	        self.pattern.add_track(midinotes)

```
## Alive Mutants
