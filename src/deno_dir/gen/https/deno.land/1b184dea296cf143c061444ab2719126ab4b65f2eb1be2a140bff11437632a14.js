const base64_code = "./ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789".split("");
const index_64 = new Uint8Array([
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    0,
    1,
    54,
    55,
    56,
    57,
    58,
    59,
    60,
    61,
    62,
    63,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    12,
    13,
    14,
    15,
    16,
    17,
    18,
    19,
    20,
    21,
    22,
    23,
    24,
    25,
    26,
    27,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    28,
    29,
    30,
    31,
    32,
    33,
    34,
    35,
    36,
    37,
    38,
    39,
    40,
    41,
    42,
    43,
    44,
    45,
    46,
    47,
    48,
    49,
    50,
    51,
    52,
    53,
    -1,
    -1,
    -1,
    -1,
    -1,
]);
export function encode(d, len) {
    let off = 0;
    let rs = [];
    let c1 = 0;
    let c2 = 0;
    while (off < len) {
        c1 = d[off++] & 0xff;
        rs.push(base64_code[(c1 >> 2) & 0x3f]);
        c1 = (c1 & 0x03) << 4;
        if (off >= len) {
            rs.push(base64_code[c1 & 0x3f]);
            break;
        }
        c2 = d[off++] & 0xff;
        c1 |= (c2 >> 4) & 0x0f;
        rs.push(base64_code[c1 & 0x3f]);
        c1 = (c2 & 0x0f) << 2;
        if (off >= len) {
            rs.push(base64_code[c1 & 0x3f]);
            break;
        }
        c2 = d[off++] & 0xff;
        c1 |= (c2 >> 6) & 0x03;
        rs.push(base64_code[c1 & 0x3f]);
        rs.push(base64_code[c2 & 0x3f]);
    }
    return rs.join("");
}
function char64(x) {
    if (x.length > 1) {
        throw new Error("Expected a single character");
    }
    let characterAsciiCode = x.charCodeAt(0);
    if (characterAsciiCode < 0 || characterAsciiCode > index_64.length)
        return -1;
    return index_64[characterAsciiCode];
}
export function decode(s, maxolen) {
    let rs = [];
    let off = 0;
    let slen = s.length;
    let olen = 0;
    let ret;
    let c1, c2, c3, c4, o;
    if (maxolen <= 0)
        throw new Error("Invalid maxolen");
    while (off < slen - 1 && olen < maxolen) {
        c1 = char64(s.charAt(off++));
        c2 = char64(s.charAt(off++));
        if (c1 === -1 || c2 === -1)
            break;
        o = c1 << 2;
        o |= (c2 & 0x30) >> 4;
        rs.push(o);
        if (++olen >= maxolen || off >= slen)
            break;
        c3 = char64(s.charAt(off++));
        if (c3 === -1)
            break;
        o = (c2 & 0x0f) << 4;
        o |= (c3 & 0x3c) >> 2;
        rs.push(o);
        if (++olen >= maxolen || off >= slen)
            break;
        c4 = char64(s.charAt(off++));
        o = (c3 & 0x03) << 6;
        o |= c4;
        rs.push(o);
        ++olen;
    }
    ret = new Uint8Array(olen);
    for (off = 0; off < olen; off++)
        ret[off] = rs[off];
    return ret;
}
//# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiYmFzZTY0LmpzIiwic291cmNlUm9vdCI6IiIsInNvdXJjZXMiOlsiaHR0cHM6Ly9kZW5vLmxhbmQveC9iY3J5cHRAdjAuMi40L3NyYy9iY3J5cHQvYmFzZTY0LnRzIl0sIm5hbWVzIjpbXSwibWFwcGluZ3MiOiJBQUFBLE1BQU0sV0FBVyxHQUNmLGtFQUFrRSxDQUFDLEtBQUssQ0FDdEUsRUFBRSxDQUNILENBQUM7QUFFSixNQUFNLFFBQVEsR0FBRyxJQUFJLFVBQVUsQ0FBQztJQUM5QixDQUFDLENBQUM7SUFDRixDQUFDLENBQUM7SUFDRixDQUFDLENBQUM7SUFDRixDQUFDLENBQUM7SUFDRixDQUFDLENBQUM7SUFDRixDQUFDLENBQUM7SUFDRixDQUFDLENBQUM7SUFDRixDQUFDLENBQUM7SUFDRixDQUFDLENBQUM7SUFDRixDQUFDLENBQUM7SUFDRixDQUFDLENBQUM7SUFDRixDQUFDLENBQUM7SUFDRixDQUFDLENBQUM7SUFDRixDQUFDLENBQUM7SUFDRixDQUFDLENBQUM7SUFDRixDQUFDLENBQUM7SUFDRixDQUFDLENBQUM7SUFDRixDQUFDLENBQUM7SUFDRixDQUFDLENBQUM7SUFDRixDQUFDLENBQUM7SUFDRixDQUFDLENBQUM7SUFDRixDQUFDLENBQUM7SUFDRixDQUFDLENBQUM7SUFDRixDQUFDLENBQUM7SUFDRixDQUFDLENBQUM7SUFDRixDQUFDLENBQUM7SUFDRixDQUFDLENBQUM7SUFDRixDQUFDLENBQUM7SUFDRixDQUFDLENBQUM7SUFDRixDQUFDLENBQUM7SUFDRixDQUFDLENBQUM7SUFDRixDQUFDLENBQUM7SUFDRixDQUFDLENBQUM7SUFDRixDQUFDLENBQUM7SUFDRixDQUFDLENBQUM7SUFDRixDQUFDLENBQUM7SUFDRixDQUFDLENBQUM7SUFDRixDQUFDLENBQUM7SUFDRixDQUFDLENBQUM7SUFDRixDQUFDLENBQUM7SUFDRixDQUFDLENBQUM7SUFDRixDQUFDLENBQUM7SUFDRixDQUFDLENBQUM7SUFDRixDQUFDLENBQUM7SUFDRixDQUFDLENBQUM7SUFDRixDQUFDLENBQUM7SUFDRixDQUFDO0lBQ0QsQ0FBQztJQUNELEVBQUU7SUFDRixFQUFFO0lBQ0YsRUFBRTtJQUNGLEVBQUU7SUFDRixFQUFFO0lBQ0YsRUFBRTtJQUNGLEVBQUU7SUFDRixFQUFFO0lBQ0YsRUFBRTtJQUNGLEVBQUU7SUFDRixDQUFDLENBQUM7SUFDRixDQUFDLENBQUM7SUFDRixDQUFDLENBQUM7SUFDRixDQUFDLENBQUM7SUFDRixDQUFDLENBQUM7SUFDRixDQUFDLENBQUM7SUFDRixDQUFDLENBQUM7SUFDRixDQUFDO0lBQ0QsQ0FBQztJQUNELENBQUM7SUFDRCxDQUFDO0lBQ0QsQ0FBQztJQUNELENBQUM7SUFDRCxDQUFDO0lBQ0QsQ0FBQztJQUNELEVBQUU7SUFDRixFQUFFO0lBQ0YsRUFBRTtJQUNGLEVBQUU7SUFDRixFQUFFO0lBQ0YsRUFBRTtJQUNGLEVBQUU7SUFDRixFQUFFO0lBQ0YsRUFBRTtJQUNGLEVBQUU7SUFDRixFQUFFO0lBQ0YsRUFBRTtJQUNGLEVBQUU7SUFDRixFQUFFO0lBQ0YsRUFBRTtJQUNGLEVBQUU7SUFDRixFQUFFO0lBQ0YsRUFBRTtJQUNGLENBQUMsQ0FBQztJQUNGLENBQUMsQ0FBQztJQUNGLENBQUMsQ0FBQztJQUNGLENBQUMsQ0FBQztJQUNGLENBQUMsQ0FBQztJQUNGLENBQUMsQ0FBQztJQUNGLEVBQUU7SUFDRixFQUFFO0lBQ0YsRUFBRTtJQUNGLEVBQUU7SUFDRixFQUFFO0lBQ0YsRUFBRTtJQUNGLEVBQUU7SUFDRixFQUFFO0lBQ0YsRUFBRTtJQUNGLEVBQUU7SUFDRixFQUFFO0lBQ0YsRUFBRTtJQUNGLEVBQUU7SUFDRixFQUFFO0lBQ0YsRUFBRTtJQUNGLEVBQUU7SUFDRixFQUFFO0lBQ0YsRUFBRTtJQUNGLEVBQUU7SUFDRixFQUFFO0lBQ0YsRUFBRTtJQUNGLEVBQUU7SUFDRixFQUFFO0lBQ0YsRUFBRTtJQUNGLEVBQUU7SUFDRixFQUFFO0lBQ0YsQ0FBQyxDQUFDO0lBQ0YsQ0FBQyxDQUFDO0lBQ0YsQ0FBQyxD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