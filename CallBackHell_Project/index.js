// Task: Food Order Processing
// Copy text
// ack Hell
// Create a JavaScript program that simulates an online food-order process using setTimeout() and nested callbacks.
// Requirements
// 1 Login the user after 1 second.
// 2 Select a food item after 2 seconds.
// 3 Place the order after 1 second.
// 4 Process the payment after 2 seconds.
// 5 Prepare the food after 3 seconds.
// 6 Deliver the order after 2 seconds.
// Functions to Create
// loginUser()
// selectFood()
// placeOrder()
//processPayment()
//perpareFood()
//deliverOrder()

//1.
const loginUser = (username, password, callback) =>{
    setTimeout(() => {
        console.log(`User ${username} logged in successfully.`);
        callback();
    }, 1000);
}
//2.
const selectFoodItem = (foodItem, callback) =>{
    setTimeout(() =>{
        console.log(`food item ${foodItem} sekectedd.`);
        callback();
    }, 2000);
}
//3.
const placeOrder = (orderId, callback) =>{
    setTimeout(() =>{
        console.log(`order ${orderId} placed.`);
        callback();
    }, 1000);
}
//4.
const processPayment = (paymaentID, callback)=>{
    setTimeout(() =>{
        console.log(`payment ${paymaentID} processedd.`);
        callback();

    },2000);
}
//5.
const prepareFood = (foodItem, callback) =>{
    setTimeout(()=>{
        console.log(`food item ${foodItem} prepared.`);
        callback();
    },3000)
}
//6.
const devliverOrder = (deliverItem, callback) =>{
    setTimeout(() => {
        console.log(`Delivering ${deliverItem}.`);
        callback();
    }, 2000);
}


loginUser("Arin", "123456789", () =>{
    selectFoodItem("Pizza", () =>{
        placeOrder("12345", () =>{
            processPayment("98765", () =>{
                prepareFood("Pizza", () =>{
                    devliverOrder("Pizza", () =>{
                        console.log("Order completed successfully!");
                    });
                });
            });
        });
    });
})