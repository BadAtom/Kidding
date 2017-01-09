module runnable;

import std.stdio, std.string, std.conv, core.stdc.stdlib, std.container: Array;

void main(string[] args)
{
	string imProg = "I'm learning to programming on ";
    auto codes = new string[1];
    codes[0] = "C";
    codes ~= "C++";
    codes ~= "D";
    codes ~= "Java";
    codes ~= "Pearl";
    codes ~= "%language%";

    for (int i = 0, n = codes.length; i < n; i++) {
        customprinter(imProg, codes[i]);
    }
}

void customprinter(string string1, string string2) {
    writeln(string1, string2);
}
