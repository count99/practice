<?php

namespace App;

use Illuminate\Database\Eloquent\Model;

class Product extends Model
{
    protected $table = 'products';

    public function picture()
    {
        return $this->hasMany('App\Picture');
    }

    public function order()
    {
        return $this->belongsTo('App\Order');
    }
}

