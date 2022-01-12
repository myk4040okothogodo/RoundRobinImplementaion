class PositionalList(_DoublyLinkedBase):
    """ A sequential container of elements allowing positional access."""
    #__________nested Position class ______________________
    class Position:
        """An abstraction representing the location of a single element."""
        def __init__(self, container, node):
            """Constructor should not be invoked by user."""
            self._container = container
            self._node = node

        def element(self):
            """Return the element stored at this Positin."""
            return self._node._element

        def __eq__(self, other):
            """Return True if other is a positon representing the same location."""
            return type(other) is type(self) and other._node is self._node

        def __ne__(self, other):
            """Return True if other doesnt represent the same loaction."""
            return not( self == other)

        #_______________utility methods ________________

        def _validate(self, p):
            """Return positions node, or raise appropriate error if invalid."""
            if not isinstance(p, self.Position):
                raise TypeError('p must be proper Positon type.')
            if p._container is not self:
                raise ValueError('p doesnt belong to this container.')
            ifp._node._next is None:               #convention for deprecated nodes
                raise ValueError('p is no longer valid')
            return p._node
        
        def _make_position(self, node):
            """Return Position instance for given node (or None if sentinel)."""
            if node is self._header or node is self._trailer:
                return None                     #bounder violation
            else:
                return self.Position(self, node) #legitimate potional

       def first(self):
           """Return the first position in the list (or None if the the list is empty)"""
           return self._make_position(self._header._next)

       def last(self):
           """Return the last Position in the list (or None if list is empty)"""
           return self._make_position(self._trailer.Prev)

       def before(self,p):
           """Return the positon just before Position p (or None if p is first)."""
           node = self._validate(p)
           return self._make_position(node._prev)

       def after(self, p):
           """ Return the position just after Position p(or None if p is last)"""
           node = self._validate(p)
           return self._make_position(node._next)
       def __iter__(self):
           """Generate a forward iteration of the eelements of the list."""
           cursor = self.first()
           while cursor is not None:
               yield cursor.element()
               cursor = self.after(cursor)

       #_______________________mutators ______________________
       #override inherited version to  return Position rather than Node

       def _insert_between(self, e, predecessor, successor):
           """Add element between existing nodes and return new Positon."""
           node = super()._insert_between(e, predecessor, successor)
           return self._make_position(node)

       def add_first(self, e):
           """Insert element e at the front of the list and return a new Position."""
           return self._insert_between(e, self._header, self._header._next)

       def add_last(self, e):
           """Insert element e  at the back of the list and return new Position."""
           return self._insert_between(e, self._trailer._prev, self._trailer)
       
       def add_before(self, p, e):
           """Insert element e into the list and return new Position."""
           original = self._validate(p)
           return self._insert_between(e, original._prev, original)
       def add_after(self, p, e):
           """Insert element e into the list after position p and return new Positon."""
           original = self._validate(p)
           return self._insert_between(e, original, original._next)
       def delete(self, p):
           """ Remove and return the element at Position p."""
           original = self._validate(p)
           return self._delete_node(original)  # inherited method return element
       def replace(self, p, e):
           """Replace the element at position p with e.
            Return the element formerly at Position p.
           """
           original = self._validate(p)
           old_value = original._element   # temporarily store old element
           old_value = original._element
           original._element = e
           return old_value


           
