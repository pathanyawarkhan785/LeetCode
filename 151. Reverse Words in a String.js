var reverseWords = function (s) {
    return s
        .split(' ')
        .filter((str) => /\w+/.test(str))
        .reverse()
        .join(' ');
};

console.log(reverseWords('a good   example'));
