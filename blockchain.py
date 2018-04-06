class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_transactions = []

    def new_block(self):
        """
        Creates new block and add to chain
        chain - self.chain
        """
        pass

    def new_transaction(self):
        """
        Adds new transaction
        """
        pass

    @staticmethod
    def hash(block):
        """
        Hashes a block
        """
        pass

    @property
    def last_block(self):
        """
        Returns the last block of the chain
        """
        pass

    def proof_of_work(self, last_proof):
        """
        This is mining.
        """
        pass

# ====================
# DEMO FRONT-END
# ====================
def manager():
	blockchain = Blockchain()
	msg = """
		Basic implementation of a Blockchain.
		Action set:
			- add message to the last block  (1)
			- add existing block to the chain    (2)
			- show a block (index will be asked) (3)
			- show the whole chain               (4)
			- validate the chain integrity       (5)
			- exit the program                   (6)
		The validate action will kill the program if the integrity if the chain
		is compromised.
		"""
	print(msg)
	while True:
		print()

		decide = input("Your action: ")

		if decide == "1":
			blockchain.add_message(Message(input("Enter your data:")))

		elif decide == "2":
			blockchain.new_block(block)

		elif decide == "3":
			index = int(input("Index: "))
			if len(blockchain.chain) > 0:
				try:
                    print(blockchain.chain[index])
				except:
                    print("Index out of range")

		elif decide == "4":
			for b in chain.chain:
				print(b "\n")
				print("----------------\n")

		elif decide == "5":
            print("Blockchain's integrity is validated")

        elif decide == "6":
            break

		else:
			print("This is not a right command")

if __name__ == "__main__":
	manager()
