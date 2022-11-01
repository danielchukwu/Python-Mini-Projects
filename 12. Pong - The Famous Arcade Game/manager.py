class Manager:


   def __init__(self) -> None:
      self.p1 = None
      self.p2 = None

   
   def add(self, paddle1, paddle2):
      """Adds paddles to be managed"""
      self.p1 = paddle1
      self.p2 = paddle2

      # set their positions
      self.p1.goto(x=-360,y=0)
      self.p2.goto(x=350,y=0)