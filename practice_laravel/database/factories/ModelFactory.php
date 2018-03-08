<?php

/*
|--------------------------------------------------------------------------
| Model Factories
|--------------------------------------------------------------------------
|
| Here you may define all of your model factories. Model factories give
| you a convenient way to create models for testing and seeding your
| database. Just tell the factory how a default model should look.
|
*/

/** @var \Illuminate\Database\Eloquent\Factory $factory */

$factory->define(App\User::class, function (Faker\Generator $faker) {
    static $password;
    return [
        'name' => $faker->name,
        'email' => $faker->unique()->safeEmail,
        'password' => $password ?: $password = bcrypt('secret'),
        'type' => random_int(0,9),
        'provider' => str_random(6),
        'remember_token' => str_random(10),
    ];
});

$factory->define(App\Buyer::class, function (Faker\Generator $faker) {
    return [
        'name' => $faker->name,
        'email' => $faker->unique()->safeEmail,
        'cellphone' => $faker->unique()->phoneNumber,
        'address' => $faker->unique()->address,
        'note' => $faker->text,
        'last_ip' => $faker->ipv4,
        'remember_token' => str_random(10),
    ];
});

$factory->define(App\Order::class, function (Faker\Generator $faker) {
    static $price;
    static $values;

    return [
        'order_index' => str_random(10),
        'name' => function(){return factory(App\Buyer::class)->make()->name;} ,
        'cellphone' => function(){return factory(App\Buyer::class)->create()->cellphone;} ,
        'product_name' => function(){return factory(App\Product::class)->create()->product_name;} ,
        'payment_way' => $faker->randomElement($array=array('貨到付款', 'ATM轉帳付款')),
        'price' => $faker->numberBetween(100,10000),
        'values' => $faker->numberBetween(1,10),
        'amounts' => $price * $values,
        'last_ip' => $faker->ipv4,
    ];
});

$factory->define(App\Product::class, function (Faker\Generator $faker) {
    return [
        'product_name' => $faker->userName,
        'price' => $faker->numberBetween(100,10000),
        'firm_name' => $faker->companySuffix,
        'url' => $faker->url,
    ];
});