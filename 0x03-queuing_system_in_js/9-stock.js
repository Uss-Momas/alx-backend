const listProducts = [
    { itemId: 1, itemName: 'Suitcase 250', price: 50, initialAvailableQuantity: 4 },
    { itemId: 2, itemName: 'Suitcase 450', price: 100, initialAvailableQuantity: 10 },
    { itemId: 3, itemName: 'Suitcase 650', price: 350, initialAvailableQuantity: 2 },
    { itemId: 4, itemName: 'Suitcase 1050', price: 550, initialAvailableQuantity: 5 },
];

const util = require('util');

const redis = require('redis');

// const redisClient = redis.createClient();

const express = require('express');

const app = express();


function getItemById(id) {
    return listProducts.find((product) => product.itemId === id);
}

function reserveStockById(itemId, stock) {
    redisClient.set(`item.${itemId}`, stock, print);
}

async function getCurrentReservedStockById(itemId) {
    const redisGet = util.promisify(redisClient.GET).bind(redisClient);
    const stock = await redisGet(`item.${itemId}`);
    return stock;
}

app.get('/list_products', (request, response) => {
    return response.json(listProducts);
});

app.get('/list_products/:itemId', async (request, response) => {
    const { itemId } = request.params;
    const product = getItemById(parseInt(itemId));
    if (!product) {
        return response.status(404).json({status: "Product not found"});
    };
    const currentStock = getCurrentReservedStockById(itemId);
    return response.json(product);
});


app.get('reserve_product/:itemId', async (request, response) => {
    const { itemId } = request.params;
    const product = getItemById(parseInt(itemId));
    if (!product) {
        return response.status(404).json({status: "Product not found"});
    };
});

app.listen(1245, '0.0.0.0', () => {
    console.log(`Server running at port 1245`);
});