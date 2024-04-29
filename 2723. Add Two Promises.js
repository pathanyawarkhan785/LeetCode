var addTwoPromises = async function (promise1, promise2) {
    // console.log(await promise1);
    // console.log(await promise2);
    return (await promise1) + (await promise2);
};

addTwoPromises(
    new Promise((resolve) => setTimeout(() => resolve(2), 20)),
    new Promise((resolve) => setTimeout(() => resolve(5), 60)),
);

/**
 * addTwoPromises(Promise.resolve(2), Promise.resolve(2))
 *   .then(console.log); // 4
 */
