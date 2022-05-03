const express = require("express")

app = express()

app.use(express.json())

const products = []
let id = 0 

function getProductById(id){
    for(let product of products){
        if (product.id == id){
            return product
        }
    }
    return {}
}

function getProductIndexById(id){
    for(let i = 0; i < products.length; i++){
        if (products[i].id == id){
            return i
        }
    }
    return -1
}

app.get("/", (req, res) =>{
    response.send("okay")
})

app.get("/products", (req, res) =>{
    res.json(products)
})

app.get("/products/:id", (req, res) =>{
    const {id} = req.params
    res.json(getProductById(id))
})

app.post("/products", (req, res) =>{
    const {name, price} = req.body
    const product = {
        id: id+=1,
        name,
        price
    }
    products.push(product)
    res.json(product)
})

app.put("/products/:id", (req, res) =>{
    const {id} = req.params
    const {name, price} = req.body
    const product = getProductById(id)
    product.name = name
    product.price = price
    res.json(product)
})

app.delete("/products/:id", (req, res) =>{
    const {id} = req.params
    const product = getProductById(id)
    const index = getProductIndexById(id)
    console.log(index)
    if (index >= 0){
        console.log("removeu")
        res.json(products.splice(index, 1))
    }else{
        res.json(product)
    }
})

app.listen(8000, "localhost")