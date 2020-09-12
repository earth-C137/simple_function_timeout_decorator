# simple_function_timeout_decorator
A simple function timeout decorator.

Seriousy, you have no idea how difficult this was to find or make.  There are modules you can import...tried one, didn't work.  Threading is hard to return the function, multiprocessing pool uses pickle and causes problems at times, concurrent futures was troublesome for some reason.

I ended up with this, I have no clue what versions it works with other than 3.7.  It's also not fully tested, so it might cause problems I'm unaware of.
