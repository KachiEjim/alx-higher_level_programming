#!/usr/bin/node

exports.esrever = function (list) {
    const newArray = [];

    for (const item of list){
        newArray.unshift(item);
    }
    return newArray
}
