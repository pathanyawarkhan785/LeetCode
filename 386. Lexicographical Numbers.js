var lexicalOrder = function (n) {
    temp = [];
    for (let i = 1; i <= n; i++) {
        temp.push(i);
    }
    return temp.sort();
};
lexicalOrder(13);
