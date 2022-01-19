



# /home/ubuntu/projects/pippin_nano_wallet/pippin/util/nano_util.py

## Newly Killed Mutants

## Alive Mutants
  
Lines 14:20

```diff
	
	    @classmethod
	    def instance(cls, max_work_processes: int = 1, max_sign_threads: int = 1) -> 'NanoUtil':
-	        if cls._instance is None:
+	        if True:
	            cls._instance = cls.__new__(cls)
	            work_processes = max(config.Config.instance().max_work_processes, 0)
	            if work_processes > 0:

```  
Lines 17:23

```diff
	        if cls._instance is None:
	            cls._instance = cls.__new__(cls)
	            work_processes = max(config.Config.instance().max_work_processes, 0)
-	            if work_processes > 0:
+	            if (work_processes >= 0):
	                cls.process_pool = ProcessPoolExecutor(max_workers=work_processes)
	            else:
	                cls.process_pool = None

```  
Lines 17:23

```diff
	        if cls._instance is None:
	            cls._instance = cls.__new__(cls)
	            work_processes = max(config.Config.instance().max_work_processes, 0)
-	            if work_processes > 0:
+	            if (work_processes != 0):
	                cls.process_pool = ProcessPoolExecutor(max_workers=work_processes)
	            else:
	                cls.process_pool = None

```  
Lines 17:23

```diff
	        if cls._instance is None:
	            cls._instance = cls.__new__(cls)
	            work_processes = max(config.Config.instance().max_work_processes, 0)
-	            if work_processes > 0:
+	            if True:
	                cls.process_pool = ProcessPoolExecutor(max_workers=work_processes)
	            else:
	                cls.process_pool = None

```  
Lines 27:33

```diff
	
	    @classmethod
	    async def close(cls):
-	        if hasattr(cls, 'process_pool') and cls.process_pool is not None:
+	        if hasattr(cls, 'process_pool') and cls.process_pool is not (False):
	            cls.process_pool.shutdown()
	        if hasattr(cls, 'thread_pool') and cls.thread_pool is not None:
	            cls.thread_pool.shutdown()

```  
Lines 27:33

```diff
	
	    @classmethod
	    async def close(cls):
-	        if hasattr(cls, 'process_pool') and cls.process_pool is not None:
+	        if hasattr(cls, 'process_pool') and cls.process_pool is not (True):
	            cls.process_pool.shutdown()
	        if hasattr(cls, 'thread_pool') and cls.thread_pool is not None:
	            cls.thread_pool.shutdown()

```  
Lines 27:33

```diff
	
	    @classmethod
	    async def close(cls):
-	        if hasattr(cls, 'process_pool') and cls.process_pool is not None:
+	        if True:
	            cls.process_pool.shutdown()
	        if hasattr(cls, 'thread_pool') and cls.thread_pool is not None:
	            cls.thread_pool.shutdown()

```  
Lines 27:33

```diff
	
	    @classmethod
	    async def close(cls):
-	        if hasattr(cls, 'process_pool') and cls.process_pool is not None:
+	        if (hasattr(cls, 'process_pool') or cls.process_pool is not None):
	            cls.process_pool.shutdown()
	        if hasattr(cls, 'thread_pool') and cls.thread_pool is not None:
	            cls.thread_pool.shutdown()

```  
Lines 29:35

```diff
	    async def close(cls):
	        if hasattr(cls, 'process_pool') and cls.process_pool is not None:
	            cls.process_pool.shutdown()
-	        if hasattr(cls, 'thread_pool') and cls.thread_pool is not None:
+	        if hasattr(cls, 'thread_pool') and (cls.thread_pool is None):
	            cls.thread_pool.shutdown()
	        if cls._instance is not None:
	            cls._instance = None

```  
Lines 29:35

```diff
	    async def close(cls):
	        if hasattr(cls, 'process_pool') and cls.process_pool is not None:
	            cls.process_pool.shutdown()
-	        if hasattr(cls, 'thread_pool') and cls.thread_pool is not None:
+	        if (hasattr(cls, 'thread_pool') or cls.thread_pool is not None):
	            cls.thread_pool.shutdown()
	        if cls._instance is not None:
	            cls._instance = None

```  
Lines 29:35

```diff
	    async def close(cls):
	        if hasattr(cls, 'process_pool') and cls.process_pool is not None:
	            cls.process_pool.shutdown()
-	        if hasattr(cls, 'thread_pool') and cls.thread_pool is not None:
+	        if hasattr(cls, 'thread_pool') and cls.thread_pool is not (False):
	            cls.thread_pool.shutdown()
	        if cls._instance is not None:
	            cls._instance = None

```  
Lines 29:35

```diff
	    async def close(cls):
	        if hasattr(cls, 'process_pool') and cls.process_pool is not None:
	            cls.process_pool.shutdown()
-	        if hasattr(cls, 'thread_pool') and cls.thread_pool is not None:
+	        if hasattr(cls, 'thread_pool') and cls.thread_pool is not (True):
	            cls.thread_pool.shutdown()
	        if cls._instance is not None:
	            cls._instance = None

```  
Lines 29:35

```diff
	    async def close(cls):
	        if hasattr(cls, 'process_pool') and cls.process_pool is not None:
	            cls.process_pool.shutdown()
-	        if hasattr(cls, 'thread_pool') and cls.thread_pool is not None:
+	        if True:
	            cls.thread_pool.shutdown()
	        if cls._instance is not None:
	            cls._instance = None

```  
Lines 29:35

```diff
	    async def close(cls):
	        if hasattr(cls, 'process_pool') and cls.process_pool is not None:
	            cls.process_pool.shutdown()
-	        if hasattr(cls, 'thread_pool') and cls.thread_pool is not None:
+	        if False:
	            cls.thread_pool.shutdown()
	        if cls._instance is not None:
	            cls._instance = None

```  
Lines 31:37

```diff
	            cls.process_pool.shutdown()
	        if hasattr(cls, 'thread_pool') and cls.thread_pool is not None:
	            cls.thread_pool.shutdown()
-	        if cls._instance is not None:
+	        if (cls._instance is None):
	            cls._instance = None
	
	    async def work_generate(self, hash: str, difficulty: str = None) -> str:

```  
Lines 31:37

```diff
	            cls.process_pool.shutdown()
	        if hasattr(cls, 'thread_pool') and cls.thread_pool is not None:
	            cls.thread_pool.shutdown()
-	        if cls._instance is not None:
+	        if True:
	            cls._instance = None
	
	    async def work_generate(self, hash: str, difficulty: str = None) -> str:

```  
Lines 31:37

```diff
	            cls.process_pool.shutdown()
	        if hasattr(cls, 'thread_pool') and cls.thread_pool is not None:
	            cls.thread_pool.shutdown()
-	        if cls._instance is not None:
+	        if False:
	            cls._instance = None
	
	    async def work_generate(self, hash: str, difficulty: str = None) -> str:

```  
Lines 31:37

```diff
	            cls.process_pool.shutdown()
	        if hasattr(cls, 'thread_pool') and cls.thread_pool is not None:
	            cls.thread_pool.shutdown()
-	        if cls._instance is not None:
+	        if cls._instance is not (False):
	            cls._instance = None
	
	    async def work_generate(self, hash: str, difficulty: str = None) -> str:

```  
Lines 31:37

```diff
	            cls.process_pool.shutdown()
	        if hasattr(cls, 'thread_pool') and cls.thread_pool is not None:
	            cls.thread_pool.shutdown()
-	        if cls._instance is not None:
+	        if cls._instance is not (True):
	            cls._instance = None
	
	    async def work_generate(self, hash: str, difficulty: str = None) -> str:

```  
Lines 32:38

```diff
	        if hasattr(cls, 'thread_pool') and cls.thread_pool is not None:
	            cls.thread_pool.shutdown()
	        if cls._instance is not None:
-	            cls._instance = None
+	            cls._instance = (False)
	
	    async def work_generate(self, hash: str, difficulty: str = None) -> str:
	        """Run work_generate in ProcessPool"""

```  
Lines 32:38

```diff
	        if hasattr(cls, 'thread_pool') and cls.thread_pool is not None:
	            cls.thread_pool.shutdown()
	        if cls._instance is not None:
-	            cls._instance = None
+	            cls._instance = (True)
	
	    async def work_generate(self, hash: str, difficulty: str = None) -> str:
	        """Run work_generate in ProcessPool"""

```  
Lines 34:40

```diff
	        if cls._instance is not None:
	            cls._instance = None
	
-	    async def work_generate(self, hash: str, difficulty: str = None) -> str:
+	    async def work_generate(self, hash: str, difficulty: str = (False)) -> str:
	        """Run work_generate in ProcessPool"""
	        if self.process_pool is None:
	            raise WorkDisabled()

```  
Lines 34:40

```diff
	        if cls._instance is not None:
	            cls._instance = None
	
-	    async def work_generate(self, hash: str, difficulty: str = None) -> str:
+	    async def work_generate(self, hash: str, difficulty: str = (True)) -> str:
	        """Run work_generate in ProcessPool"""
	        if self.process_pool is None:
	            raise WorkDisabled()

```  
Lines 36:42

```diff
	
	    async def work_generate(self, hash: str, difficulty: str = None) -> str:
	        """Run work_generate in ProcessPool"""
-	        if self.process_pool is None:
+	        if self.process_pool is (False):
	            raise WorkDisabled()
	
	        difficulty = difficulty if difficulty is not None else nanopy.work_difficulty

```  
Lines 36:42

```diff
	
	    async def work_generate(self, hash: str, difficulty: str = None) -> str:
	        """Run work_generate in ProcessPool"""
-	        if self.process_pool is None:
+	        if self.process_pool is (True):
	            raise WorkDisabled()
	
	        difficulty = difficulty if difficulty is not None else nanopy.work_difficulty

```  
Lines 36:42

```diff
	
	    async def work_generate(self, hash: str, difficulty: str = None) -> str:
	        """Run work_generate in ProcessPool"""
-	        if self.process_pool is None:
+	        if False:
	            raise WorkDisabled()
	
	        difficulty = difficulty if difficulty is not None else nanopy.work_difficulty

```  
Lines 39:45

```diff
	        if self.process_pool is None:
	            raise WorkDisabled()
	
-	        difficulty = difficulty if difficulty is not None else nanopy.work_difficulty
+	        difficulty = difficulty if (difficulty is None) else nanopy.work_difficulty
	        result = await asyncio.get_event_loop().run_in_executor(
	            self.process_pool,
	            functools.partial(

```  
Lines 39:45

```diff
	        if self.process_pool is None:
	            raise WorkDisabled()
	
-	        difficulty = difficulty if difficulty is not None else nanopy.work_difficulty
+	        difficulty = difficulty if difficulty is not (False) else nanopy.work_difficulty
	        result = await asyncio.get_event_loop().run_in_executor(
	            self.process_pool,
	            functools.partial(

```  
Lines 39:45

```diff
	        if self.process_pool is None:
	            raise WorkDisabled()
	
-	        difficulty = difficulty if difficulty is not None else nanopy.work_difficulty
+	        difficulty = difficulty if difficulty is not (True) else nanopy.work_difficulty
	        result = await asyncio.get_event_loop().run_in_executor(
	            self.process_pool,
	            functools.partial(

```