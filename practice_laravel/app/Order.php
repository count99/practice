<?php

namespace App;

use Illuminate\Database\Eloquent\Model;

class Order extends Model
{
    protected $table = 'orders';

    public function buyer()
    {
        return $this->hasOne('App\Buyer', 'name');
    }

    public function product()
    {
        return $this->hasOne('App\Product', 'product_name');
    }
}
