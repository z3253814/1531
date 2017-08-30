class Question:
	def __init__ (self, question, answers):
		self.question = question
		self.answers = answers
	def print_q(self):
		print self.question
		print self.answers
		
q_input = "hi"
a_input =  ["hi", "bye"]
q = Question(q_input, a_input)

q.print_q()
