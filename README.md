# Timezoner

## Get the timezone for an epoch time with zipcode.

### Usage

    timezone_est(time, loc)

`time` is a string which contains the epoch time in milliseconds

`loc` is a string that contains the zip code (e.g. '94115') and state abbreviation (e.g. ', CA ') separated by a comma

`timezone_est` returns a [struct_time](http://docs.python.org/2/library/time.html#time.struct_time) object

### Example

    timezone_est('1391898323633', '94115, CA')
    
will return

    time.struct_time(tm_year=2014, tm_mon=2, tm_mday=8, tm_hour=17, tm_min=25, tm_sec=23, tm_wday=5, tm_yday=39, tm_isdst=0)

## License

The MIT License (MIT)

Copyright (c) 2013 Automatic Inc

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
