from models import storage
from models.user import User
from models.state import State

s = State()

s.name = "Kenya"

print(s)

s.save()