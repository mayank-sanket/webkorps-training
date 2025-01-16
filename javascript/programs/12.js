const st = new Set(['a', 'b', 'a', 'c', 'd'])
console.log(st)
st.add("e")
st.add("e")
st.add("f")
console.log(st)


console.log(st.has("f")) // true


st.forEach((a) => console.log(a))


const otherst = new Set(['a', 'b', 'c', 'd'])

const myIterator = otherst.values()

for(it of myIterator){
    console.log(it)
}


const newotherset = new Set([1, 2, 3, 4, 5, 6])
const myIt2 = newotherset.values()

for(it of myIt2){
    console.log(it)
}

const xyz = new Set([1, 2, 3453,343])
const myit3 = xyz.entries()

for(it of myit3){
console.log(it)  // [1,1] [2,2] [3453, 3453] [343, 343]

}