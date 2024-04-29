var ArrayWrapper = function (nums, opr) {
    let sum = 0;
    nums.forEach((num) => {
        sum += num;
    });
    console.log(sum);
    if (opr == 'Add') {
    }

    // console.log(nums, opr);
};
ArrayWrapper(
    [
        [1, 2],
        [3, 4],
    ],
    'Add',
);
