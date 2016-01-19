from .misc.makeapi import make_api, Move

moves = [
	Move('misc.trim', 'misc.trim_docstring')
]

exclude = ['test', 'version']

make_api(__name__, __file__, __package__, exclude=exclude, moves=moves)

__path__ = []

__package__ = __name__  # see PEP 366 @ReservedAssignment
if globals().get("__spec__") is not None:
	 __spec__.submodule_search_locations = []  # PEP 451 @UndefinedVariable

