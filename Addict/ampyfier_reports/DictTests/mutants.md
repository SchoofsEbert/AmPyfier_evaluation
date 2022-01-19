



# /home/ubuntu/projects/addict/addict/addict.py

## Newly Killed Mutants

### test_init_raises_none_1
  
Lines 8:14

```diff
	        object.__setattr__(__self, '__key', kwargs.pop('__key', None))
	        object.__setattr__(__self, '__frozen', False)
	        for arg in args:
-	            if not arg:
+	            if False:
	                continue
	            elif isinstance(arg, dict):
	                for key, val in arg.items():

```
### test_to_dict_none_1_none_6
  
Lines 77:83

```diff
	    def to_dict(self):
	        base = {}
	        for key, value in self.items():
-	            if isinstance(value, type(self)):
+	            if False:
	                base[key] = value.to_dict()
	            elif isinstance(value, (list, tuple)):
	                base[key] = type(value)(

```
## Alive Mutants
  
Lines 5:11

```diff
	
	    def __init__(__self, *args, **kwargs):
	        object.__setattr__(__self, '__parent', kwargs.pop('__parent', None))
-	        object.__setattr__(__self, '__key', kwargs.pop('__key', None))
+	        object.__setattr__(__self, '__key', kwargs.pop('__key', (False)))
	        object.__setattr__(__self, '__frozen', False)
	        for arg in args:
	            if not arg:

```  
Lines 5:11

```diff
	
	    def __init__(__self, *args, **kwargs):
	        object.__setattr__(__self, '__parent', kwargs.pop('__parent', None))
-	        object.__setattr__(__self, '__key', kwargs.pop('__key', None))
+	        object.__setattr__(__self, '__key', kwargs.pop('__key', (True)))
	        object.__setattr__(__self, '__frozen', False)
	        for arg in args:
	            if not arg:

```  
Lines 6:12

```diff
	    def __init__(__self, *args, **kwargs):
	        object.__setattr__(__self, '__parent', kwargs.pop('__parent', None))
	        object.__setattr__(__self, '__key', kwargs.pop('__key', None))
-	        object.__setattr__(__self, '__frozen', False)
+	        object.__setattr__(__self, '__frozen', None)
	        for arg in args:
	            if not arg:
	                continue

```  
Lines 13:19

```diff
	            elif isinstance(arg, dict):
	                for key, val in arg.items():
	                    __self[key] = __self._hook(val)
-	            elif isinstance(arg, tuple) and (not isinstance(arg[0], tuple)):
+	            elif isinstance(arg, tuple) and (not isinstance(arg[<_ast.UnaryOp object at 0x7fa6f7eb0340>], tuple)):
	                __self[arg[0]] = __self._hook(arg[1])
	            else:
	                for key, val in iter(arg):

```  
Lines 13:19

```diff
	            elif isinstance(arg, dict):
	                for key, val in arg.items():
	                    __self[key] = __self._hook(val)
-	            elif isinstance(arg, tuple) and (not isinstance(arg[0], tuple)):
+	            elif isinstance(arg, tuple) and (not isinstance(arg[<_ast.Constant object at 0x7fa6f7eb03d0>], tuple)):
	                __self[arg[0]] = __self._hook(arg[1])
	            else:
	                for key, val in iter(arg):

```  
Lines 14:20

```diff
	                for key, val in arg.items():
	                    __self[key] = __self._hook(val)
	            elif isinstance(arg, tuple) and (not isinstance(arg[0], tuple)):
-	                __self[arg[0]] = __self._hook(arg[1])
+	                __self[arg[0]] = __self._hook(arg[<_ast.UnaryOp object at 0x7fa6db9fda00>])
	            else:
	                for key, val in iter(arg):
	                    __self[key] = __self._hook(val)

```  
Lines 40:46

```diff
	            key = object.__getattribute__(self, '__key')
	        except AttributeError:
	            p = None
-	            key = None
+	            key = (False)
	        if p is not None:
	            p[key] = self
	            object.__delattr__(self, '__parent')

```  
Lines 40:46

```diff
	            key = object.__getattribute__(self, '__key')
	        except AttributeError:
	            p = None
-	            key = None
+	            key = (True)
	        if p is not None:
	            p[key] = self
	            object.__delattr__(self, '__parent')

```  
Lines 103:109

```diff
	    def update(self, *args, **kwargs):
	        other = {}
	        if args:
-	            if len(args) > 1:
+	            if (len(args) != 1):
	                raise TypeError()
	            other.update(args[0])
	        other.update(kwargs)

```  
Lines 105:111

```diff
	        if args:
	            if len(args) > 1:
	                raise TypeError()
-	            other.update(args[0])
+	            other.update(args[<_ast.UnaryOp object at 0x7fa6db9fdf70>])
	        other.update(kwargs)
	        for k, v in other.items():
	            if ((k not in self) or

```  
Lines 142:148

```diff
	        self.update(other)
	        return self
	
-	    def setdefault(self, key, default=None):
+	    def setdefault(self, key, default=(False)):
	        if key in self:
	            return self[key]
	        else:

```  
Lines 142:148

```diff
	        self.update(other)
	        return self
	
-	    def setdefault(self, key, default=None):
+	    def setdefault(self, key, default=(True)):
	        if key in self:
	            return self[key]
	        else:

```  
Lines 156:159

```diff
	                val.freeze(shouldFreeze)
	
	    def unfreeze(self):
-	        self.freeze(False)
+	        self.freeze(None)
	
```
# /home/ubuntu/projects/addict/addict/__init__.py

## Newly Killed Mutants

## Alive Mutants
