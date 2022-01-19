



# /home/ubuntu/projects/python-twelve-tone/src/twelve_tone/composer.py

## Newly Killed Mutants

### test_master_numb_div_0
  
Lines 77:83

```diff
	        diff = (self.matrix[0][x + 1] - self.matrix[0][x])
	        opposite = diff * -1
	        result = opposite + self.matrix[x][0]
-	        if result in range(1, 13):
+	        if (result not in range(1, 13)):
	            self.matrix[x + 1][0] = result
	        else:
	            self.matrix[x + 1][0] = self._transform_cell(result)

```  
Lines 77:83

```diff
	        diff = (self.matrix[0][x + 1] - self.matrix[0][x])
	        opposite = diff * -1
	        result = opposite + self.matrix[x][0]
-	        if result in range(1, 13):
+	        if True:
	            self.matrix[x + 1][0] = result
	        else:
	            self.matrix[x + 1][0] = self._transform_cell(result)

```
## Alive Mutants
  
Lines 8:14

```diff
	class Composer(object):
	    matrix = np.zeros((12, 12), dtype=int)
	
-	    def compose(self, top_row=None):
+	    def compose(self, top_row=(False)):
	        # top_row
	        self._load_top_row(top_row)
	        # load first column

```  
Lines 18:24

```diff
	
	        return self.matrix
	
-	    def get_melody(self, row=0, column=None):
+	    def get_melody(self, row=0, column=(False)):
	        """
	        Returns a tone row that can be used
	        as a 12 tone melody.

```  
Lines 18:24

```diff
	
	        return self.matrix
	
-	    def get_melody(self, row=0, column=None):
+	    def get_melody(self, row=0, column=(True)):
	        """
	        Returns a tone row that can be used
	        as a 12 tone melody.

```  
Lines 75:81

```diff
	
	    def _load_col_cell(self, x):
	        diff = (self.matrix[0][x + 1] - self.matrix[0][x])
-	        opposite = diff * -1
+	        opposite = (diff // -1)
	        result = opposite + self.matrix[x][0]
	        if result in range(1, 13):
	            self.matrix[x + 1][0] = result

```  
Lines 75:81

```diff
	
	    def _load_col_cell(self, x):
	        diff = (self.matrix[0][x + 1] - self.matrix[0][x])
-	        opposite = diff * -1
+	        opposite = (diff / -1)
	        result = opposite + self.matrix[x][0]
	        if result in range(1, 13):
	            self.matrix[x + 1][0] = result

```  
Lines 77:83

```diff
	        diff = (self.matrix[0][x + 1] - self.matrix[0][x])
	        opposite = diff * -1
	        result = opposite + self.matrix[x][0]
-	        if result in range(1, 13):
+	        if False:
	            self.matrix[x + 1][0] = result
	        else:
	            self.matrix[x + 1][0] = self._transform_cell(result)

```  
Lines 87:93

```diff
	            for y in range(0, 11):
	                calc = (self.matrix[x][y] - self.matrix[x - 1][y]) \
	                    + self.matrix[x - 1][y + 1]
-	                if calc not in range(1, 13):
+	                if True:
	                    calc = self._transform_cell(calc)
	                self.matrix[x][y + 1] = calc
	

```  
Lines 94:100

```diff
	    def _transform_cell(self, cell):
	        if cell in range(1, 13):
	            return cell
-	        if cell < 0 or cell == 0:
+	        if (cell <= 0) or cell == 0:
	            return self._transform_cell(cell + 12)
	        else:
	            return self._transform_cell(cell - 12)

```  
Lines 94:100

```diff
	    def _transform_cell(self, cell):
	        if cell in range(1, 13):
	            return cell
-	        if cell < 0 or cell == 0:
+	        if cell < 0 or (cell <= 0):
	            return self._transform_cell(cell + 12)
	        else:
	            return self._transform_cell(cell - 12)

```  
Lines 97:100

```diff
	        if cell < 0 or cell == 0:
	            return self._transform_cell(cell + 12)
	        else:
-	            return self._transform_cell(cell - 12)
+	            return self._transform_cell((cell % 12))
	
```