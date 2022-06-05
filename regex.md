[abc] will match a, b, and c (every occurrence of each letter)

[abc]zz will match azz, bzz, and czz.

You can also use a - dash to define ranges:
[a-c]zz is the same as above.

And then you can combine ranges together:
[a-cx-z]zz will match azz, bzz, czz, xzz, yzz, and zzz.

Most notably, this can be used to match any alphabetical character:
[a-zA-Z] will match any single letter (lowercase or uppercase).

You can use numbers too:
file[1-3] will match file1, file2, and file3.

Then, there is a way to exclude characters from a charset with the ^ hat symbol, and include everything else.
[^k]ing will match ring, sing, $ing, but not king.

Of course, you can exclude charsets, not just single characters.
[^a-c]at will match fat and hat, but not bat or cat.
The wildcard that is used to match any single character (except the line break) is the . dot. That means that a.c will match aac, abc, a0c, a!c, and so on.

Also, you can set a character as optional in your pattern using the ? question mark. That means that abc? will match ab and abc, since the c is optional.

Note: If you want to search for . a literal dot, you have to escape it with a \ reverse slash. That means that a.c will match a.c, but also abc, a@c, and so on. But a\.c will match just a.c.

Answer the questions below
Match all of the following words: Cat, fat, hat, rat
.at
Match all of the following words: Cat, cats

.[cC]ats?
Match the following domain name: cat.xyz

cat\.xyz
Match all of the following domain names: cat.xyz, cats.xyz, hats.xyz

[ch]ats?\.xyz
Match every 4-letter string that doesn't end in any letter from n to z

...[^n-z]
Match bat, bats, hat, hats, but not rat or rats (use the hat symbol)

[^r]ats?

\d matches a digit, like 9
\D matches a non-digit, like A or @
\w matches an alphanumeric character, like a or 3
\W matches a non-alphanumeric character, like ! or #
\s matches a whitespace character (spaces, tabs, and line breaks)
\S matches everything else (alphanumeric characters and symbols)

Note: Underscores _ are included in the \w metacharacter and not in \W. That means that \w will match every single character in test_file.

Often we want a pattern that matches many characters of a single type in a row, and we can do that with repetitions. For example, {2} is used to match the preceding character (or metacharacter, or charset) two times in a row. That means that z{2} will match exactly zz.

Here's a reference for each repetition along with how many times it matches the preceding pattern:

{12} - exactly 12 times.
{1,5} - 1 to 5 times.
{2,} - 2 or more times.
* - 0 or more times.
+ - 1 or more times.