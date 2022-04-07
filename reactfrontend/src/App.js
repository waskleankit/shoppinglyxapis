//import logo from './logo.svg';
import { useState, useEffect } from "react";
import axios from "axios";
import './App.css';

function App() {
    const [customers,setCustomers] = useState([])
    useEffect(()=>{
        async function getAllCustomer(){
        try{
            const customers = await axios.get("http://127.0.0.1:8000/customer_api/customers/")
            console.log(customers.data)
            setCustomers(customers.data)
        } catch (error) {
            console.log(error)
        }
        }
        getAllCustomer()
    }, [])


  return (
    <div className="App">
        <h1> Connect React JS to Django </h1>
        {
            customers.map((customer, i)=>{
                return (
                <h2 key={i}>{customer.name}{customer.locality}{customer.city}{customer.zipcode}{customer.state}</h2>
                )
            })
        }
    </div>
  );
}

export default App;
