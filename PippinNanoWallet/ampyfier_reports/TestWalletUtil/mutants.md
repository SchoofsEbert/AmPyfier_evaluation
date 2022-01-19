



# /home/ebert/projects/pippin_nano_wallet/pippin/util/wallet.py

## Newly Killed Mutants

## Alive Mutants
  
Lines 16:22

```diff
	from pippin.network.rpc_client import AccountNotFound, RPCClient
	from pippin.network.work_client import WorkClient
	
-	if TYPE_CHECKING:
+	if True:
	    from pippin.db.models.wallet import Wallet
	
	class WalletUtil(object):

```  
Lines 16:22

```diff
	from pippin.network.rpc_client import AccountNotFound, RPCClient
	from pippin.network.work_client import WorkClient
	
-	if TYPE_CHECKING:
+	if False:
	    from pippin.db.models.wallet import Wallet
	
	class WalletUtil(object):

```  
Lines 27:33

```diff
	        self.wallet = wallet
	
	    def get_representative(self):
-	        if self.wallet.representative is None:
+	        if False:
	            return config.Config.instance().get_random_rep()
	        return self.wallet.representative
	

```  
Lines 27:33

```diff
	        self.wallet = wallet
	
	    def get_representative(self):
-	        if self.wallet.representative is None:
+	        if self.wallet.representative is (False):
	            return config.Config.instance().get_random_rep()
	        return self.wallet.representative
	

```  
Lines 27:33

```diff
	        self.wallet = wallet
	
	    def get_representative(self):
-	        if self.wallet.representative is None:
+	        if self.wallet.representative is (True):
	            return config.Config.instance().get_random_rep()
	        return self.wallet.representative
	

```  
Lines 40:46

```diff
	        return self.account.private_key(self.wallet.seed)
	
	
-	    async def publish(self, state_block: dict, subtype: str = None) -> dict:
+	    async def publish(self, state_block: dict, subtype: str = (False)) -> dict:
	        """Publish a state block"""
	        try:
	            resp = await RPCClient.instance().process(state_block, subtype=subtype)

```  
Lines 40:46

```diff
	        return self.account.private_key(self.wallet.seed)
	
	
-	    async def publish(self, state_block: dict, subtype: str = None) -> dict:
+	    async def publish(self, state_block: dict, subtype: str = (True)) -> dict:
	        """Publish a state block"""
	        try:
	            resp = await RPCClient.instance().process(state_block, subtype=subtype)

```  
Lines 52:58

```diff
	            from pippin.db.models.wallet import ProcessFailed
	            raise ProcessFailed()
	
-	    async def _receive_block_create(self, hash: str, work: str = None) -> dict:
+	    async def _receive_block_create(self, hash: str, work: str = (False)) -> dict:
	        """Build a state block (receive)"""
	        # Get block info
	        block_info = await RPCClient.instance().block_info(hash)

```  
Lines 52:58

```diff
	            from pippin.db.models.wallet import ProcessFailed
	            raise ProcessFailed()
	
-	    async def _receive_block_create(self, hash: str, work: str = None) -> dict:
+	    async def _receive_block_create(self, hash: str, work: str = (True)) -> dict:
	        """Build a state block (receive)"""
	        # Get block info
	        block_info = await RPCClient.instance().block_info(hash)

```  
Lines 104:110

```diff
	
	        return state_block
	
-	    async def receive(self, hash: str, work: str = None) -> dict:
+	    async def receive(self, hash: str, work: str = (False)) -> dict:
	        """Receive a block and return hash of published block"""
	        async with await (await RedisDB.instance().get_lock_manager()).lock(f"pippin:{self.account.address}") as lock:
	            block = await self._receive_block_create(hash, work)

```  
Lines 104:110

```diff
	
	        return state_block
	
-	    async def receive(self, hash: str, work: str = None) -> dict:
+	    async def receive(self, hash: str, work: str = (True)) -> dict:
	        """Receive a block and return hash of published block"""
	        async with await (await RedisDB.instance().get_lock_manager()).lock(f"pippin:{self.account.address}") as lock:
	            block = await self._receive_block_create(hash, work)

```  
Lines 129:135

```diff
	            received_count = await self._receive_all()
	        return received_count
	
-	    async def _send_block_create(self, amount: int, destination: str, id: str = None, work: str = None) -> dict:
+	    async def _send_block_create(self, amount: int, destination: str, id: str = None, work: str = (False)) -> dict:
	        """Create a state block (send)"""
	        # Get account info
	        account_balance = await RPCClient.instance().account_balance(self.account.address)

```  
Lines 129:135

```diff
	            received_count = await self._receive_all()
	        return received_count
	
-	    async def _send_block_create(self, amount: int, destination: str, id: str = None, work: str = None) -> dict:
+	    async def _send_block_create(self, amount: int, destination: str, id: str = None, work: str = (True)) -> dict:
	        """Create a state block (send)"""
	        # Get account info
	        account_balance = await RPCClient.instance().account_balance(self.account.address)

```  
Lines 129:135

```diff
	            received_count = await self._receive_all()
	        return received_count
	
-	    async def _send_block_create(self, amount: int, destination: str, id: str = None, work: str = None) -> dict:
+	    async def _send_block_create(self, amount: int, destination: str, id: str = (False), work: str = None) -> dict:
	        """Create a state block (send)"""
	        # Get account info
	        account_balance = await RPCClient.instance().account_balance(self.account.address)

```  
Lines 129:135

```diff
	            received_count = await self._receive_all()
	        return received_count
	
-	    async def _send_block_create(self, amount: int, destination: str, id: str = None, work: str = None) -> dict:
+	    async def _send_block_create(self, amount: int, destination: str, id: str = (True), work: str = None) -> dict:
	        """Create a state block (send)"""
	        # Get account info
	        account_balance = await RPCClient.instance().account_balance(self.account.address)

```  
Lines 185:191

```diff
	
	        return state_block
	
-	    async def send(self, amount: int, destination: str, id: str = None, work: str = None) -> dict:
+	    async def send(self, amount: int, destination: str, id: str = None, work: str = (False)) -> dict:
	        """Create a send block and return hash of published block
	            amount is in RAW"""
	        

```  
Lines 185:191

```diff
	
	        return state_block
	
-	    async def send(self, amount: int, destination: str, id: str = None, work: str = None) -> dict:
+	    async def send(self, amount: int, destination: str, id: str = None, work: str = (True)) -> dict:
	        """Create a send block and return hash of published block
	            amount is in RAW"""
	        

```  
Lines 185:191

```diff
	
	        return state_block
	
-	    async def send(self, amount: int, destination: str, id: str = None, work: str = None) -> dict:
+	    async def send(self, amount: int, destination: str, id: str = (False), work: str = None) -> dict:
	        """Create a send block and return hash of published block
	            amount is in RAW"""
	        

```  
Lines 185:191

```diff
	
	        return state_block
	
-	    async def send(self, amount: int, destination: str, id: str = None, work: str = None) -> dict:
+	    async def send(self, amount: int, destination: str, id: str = (True), work: str = None) -> dict:
	        """Create a send block and return hash of published block
	            amount is in RAW"""
	        

```  
Lines 219:225

```diff
	                    await block.save()
	            return resp
	
-	    async def _change_block_create(self, representative: str, work: str = None, only_if_different: bool = False) -> dict:
+	    async def _change_block_create(self, representative: str, work: str = (False), only_if_different: bool = False) -> dict:
	        """Create a state block (change)"""
	        # Get account info
	        account_info = await RPCClient.instance().account_info(self.account.address)

```  
Lines 219:225

```diff
	                    await block.save()
	            return resp
	
-	    async def _change_block_create(self, representative: str, work: str = None, only_if_different: bool = False) -> dict:
+	    async def _change_block_create(self, representative: str, work: str = (True), only_if_different: bool = False) -> dict:
	        """Create a state block (change)"""
	        # Get account info
	        account_info = await RPCClient.instance().account_info(self.account.address)

```  
Lines 219:225

```diff
	                    await block.save()
	            return resp
	
-	    async def _change_block_create(self, representative: str, work: str = None, only_if_different: bool = False) -> dict:
+	    async def _change_block_create(self, representative: str, work: str = None, only_if_different: bool = (True)) -> dict:
	        """Create a state block (change)"""
	        # Get account info
	        account_info = await RPCClient.instance().account_info(self.account.address)

```  
Lines 219:225

```diff
	                    await block.save()
	            return resp
	
-	    async def _change_block_create(self, representative: str, work: str = None, only_if_different: bool = False) -> dict:
+	    async def _change_block_create(self, representative: str, work: str = None, only_if_different: bool = None) -> dict:
	        """Create a state block (change)"""
	        # Get account info
	        account_info = await RPCClient.instance().account_info(self.account.address)

```  
Lines 259:265

```diff
	
	        return state_block
	
-	    async def representative_set(self, representative: str, work: str = None, only_if_different: bool = False) -> dict:
+	    async def representative_set(self, representative: str, work: str = None, only_if_different: bool = (True)) -> dict:
	        """Create a change block and return hash of published block"""
	        async with await (await RedisDB.instance().get_lock_manager()).lock(f"pippin:{self.account.address}") as lock:
	            state_block = await self._change_block_create(representative, work=work, only_if_different=only_if_different)

```  
Lines 259:265

```diff
	
	        return state_block
	
-	    async def representative_set(self, representative: str, work: str = None, only_if_different: bool = False) -> dict:
+	    async def representative_set(self, representative: str, work: str = None, only_if_different: bool = None) -> dict:
	        """Create a change block and return hash of published block"""
	        async with await (await RedisDB.instance().get_lock_manager()).lock(f"pippin:{self.account.address}") as lock:
	            state_block = await self._change_block_create(representative, work=work, only_if_different=only_if_different)

```  
Lines 259:265

```diff
	
	        return state_block
	
-	    async def representative_set(self, representative: str, work: str = None, only_if_different: bool = False) -> dict:
+	    async def representative_set(self, representative: str, work: str = (False), only_if_different: bool = False) -> dict:
	        """Create a change block and return hash of published block"""
	        async with await (await RedisDB.instance().get_lock_manager()).lock(f"pippin:{self.account.address}") as lock:
	            state_block = await self._change_block_create(representative, work=work, only_if_different=only_if_different)

```  
Lines 259:265

```diff
	
	        return state_block
	
-	    async def representative_set(self, representative: str, work: str = None, only_if_different: bool = False) -> dict:
+	    async def representative_set(self, representative: str, work: str = (True), only_if_different: bool = False) -> dict:
	        """Create a change block and return hash of published block"""
	        async with await (await RedisDB.instance().get_lock_manager()).lock(f"pippin:{self.account.address}") as lock:
	            state_block = await self._change_block_create(representative, work=work, only_if_different=only_if_different)

```