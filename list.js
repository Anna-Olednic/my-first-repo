
// @ts-check

import { readFileSync } from 'fs';

var body = readFileSync('C:\\Users\\Anna\\Desktop\\TESTING\\list_data\\listResponse.json', 'utf8'); 
const data = JSON.parse(body);

for(var i = 0; i<data.lists.length; i++){
    console.log(i)
    console.log(data.lists[i].name)
     console.log(data.lists[i].id)

    // if ((data.lists[i].name)==("List NewCody"))
    //     console.log (data.lists[i].id)
}

// console.log(data.lists)

// const arrayOfElements = [1,2,"43","34443"]

// arrayOfElements.forEach(item =>{
//     console.log(item)
// })

// const arrayOfElements = [1,2,"43",'343444']

// arrayOfElements = [0]
// arrayOfElements = [1]
// arrayOfElements = [2]