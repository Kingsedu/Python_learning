


// function runSelectionSort(arr){
//     if(arr.length <= 1) return arr
//     if(typeof arr !== 'object' && !Array.isArray(arr)){
//         return 'this is not an array'
//     }

//     for(let i = 0; i < arr.length - 1; i++){
//         let minIdx = i

//         for(let j = i + 1; j < arr.length; j++){
//             if(arr[j] > arr[minIdx]){
//                 minIdx = j
//             }
//         }
//         if(minIdx !== i){
//             [arr[i], arr[minIdx]] = [arr[minIdx], arr[i]]
//         }
//     }
//     return arr
// }

// function swapItem(arr){
//     if (!Array.isArray(arr)){

//     }
// }

// let arr_one = ["a", "b", "c", "d"]
// for(let key in arr_one){
//     console.log(arr_one[key])
// }

// console.log(10 / 2)
// let so_called_empty_string = " "

// // console.log(so_called_empty_string.length)
// const object_one = {
//     name: "chi_ned",
//     age: "still young",
//     mentality: "positive die",
//     so_delete : true
// }

// delete object_one.so_delete

// console.log(object_one)
// const object_entries = Object.entries(object_one)
// console.log(object_entries)
// for [key, value] of Object.entries(object_one){
//     console.log(key)
// }

// for ([d_key, d_value] of object_entries){
//     console.log(`this is the ${d_key} which has a corresponding value of ${d_value}`)
// }

// is_true = name in object_one

// print(is_true)

// let testingObject = {
//     name : "ned",
//     class : "big_boy",
//     fav_artist: "Mr M & revelation"
// }

// for (let key in testingObject){
//     console.log(key.toLocaleUpperCase())
// }

// let string_array = ["a", "b", "d", "a", "c", "d", "i", "g", "b"]
// const my_string_array = new Set(string_array)
// console.log(my_string_array)

// let x = [7, 8, 9]
// let y = x
// x = [13, 15, 20]

// console.log(y)

class User {
    constructor(age, size) {
       //
       this.my_age = age;
       this.my_size = size;
    }
}

const userOne = new User(10, 24)
console.log(userOne.my_age)