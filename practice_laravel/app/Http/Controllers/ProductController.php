<?php

namespace App\Http\Controllers;

use App\Order;
use App\Picture;
use App\Product;
use Illuminate\Http\Request;
use Illuminate\Routing\Controller;

class ProductController extends Controller
{
    //
    public function index($product_name)
    {
        $pictures = Picture::where("product_name","=", $product_name)->get();
        $products = Product::where("product_name", "=", $product_name)->first();
        return View('product', ['pictures'=>$pictures, 'products'=>$products, 'product_name'=>$products->product_name]);
    }

    public function newOrder(Request $request, $product_name)
    {
//        填寫訂單
        $now_time = strtotime("+6hours");
        $add_time = date("YmdHis", $now_time);
        $add_str = str_random(8);
//        產品編號
        $order_index = $add_time.$add_str;
        $products = Product::where("product_name", "=", $product_name)->first();
//        產品價格
        $price = $products->price;

//        購買人輸入資料

        $order = new Order;
        $order->order_index = $order_index;
        $order->name = $request->input('name');
        $order->cellphone = $request->input('cellphone');
        $order->product_name = $product_name;
        $order->payment_way = $request->input('payment_way');
        $order->price = $price;
        $order->values = $request->input('values');
        $amounts = $price * $request->input('values');
        $order->amounts = $amounts;
        $order->last_ip = $_SERVER['REMOTE_ADDR'];

        $order->save();

        return "訂購成功";
    }


}
