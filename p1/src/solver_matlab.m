%parameters
N = 1794;
d = 10;

syms x;
eq = 0;
for i = 1:d
    eq = eq + x^i;
end

result = vpasolve((eq - N) == 0, x);
result = double(result);
sel = result == real(result);
valid_results = result(sel)
