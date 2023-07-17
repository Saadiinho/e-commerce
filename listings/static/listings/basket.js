function saveBasket(basket){
    localStorage.setItem('basket', JSON.stringify(basket));
}

function getBasket(){
    let basket = localStorage.getItem("basket");
    if (basket == null){
        return {};
    }
    else {
        return JSON.parse(basket);
    }
}

function addBasket(){
    var basket = getBasket();
    $(document).on('click', '.ted', function(){
        console.log("ajoute");
        var item_id = this.id.toString();
        if (basket[item_id] != undefined){
            basket[item_id] += 1;
        }
        else {
            basket[item_id] = 1;
        }
        console.log(basket);
    });
    saveBasket(basket);
}

function removeFromBasket(product){
    let basket = getBasket();
    basket = basket.filter(p => p.id != product.id);
    saveBasket(basket);
}

function changeQuantity(product){
    let basket = getBasket();
    let foundProduct = basket.find(p => p.id == product.id);
    if (foundProduct != undefined) {
        foundProduct.quantity += 1;
        if(foundProduct.quantity <=0){
            removeFromBasket(foundProduct);
        }
        else {
            saveBasket(basket);
        }
    }
}

function getNumberProduct(){
    let basket = getBasket();
    let number = 0;
    for (let product of basket){
        number += product.quantity;
    }
    return number;
}

function getTotalPrice(){
    let basket = getBasket();
    let total = 0;
    for (let product of basket){
        total += product.quantity * product.price;
    }
    return total;
}

console.log("Juste pour tester");
addBasket();