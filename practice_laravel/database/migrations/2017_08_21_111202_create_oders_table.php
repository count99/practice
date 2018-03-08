<?php

use Illuminate\Support\Facades\Schema;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Database\Migrations\Migration;

class CreateOdersTable extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('orders', function (Blueprint $table) {
            $table->increments('id');
            $table->string('order_index');
            $table->string('name')->references('name')->on('buyers');
            $table->string('cellphone')->unique()->references('cellphone')->on('buyers');
            $table->string('product_name')->references('product_name')->on('products');
            $table->string('payment_way');
            $table->integer('price');
            $table->integer('values');
            $table->integer('amounts');
            $table->ipAddress('last_ip');
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::drop('orders');
    }
}
