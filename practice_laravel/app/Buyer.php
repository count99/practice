<?php

namespace App;

use Illuminate\Database\Eloquent\Model;

class Buyer extends Model
{
    protected $table = 'buyers';

    public function order()
    {
        return $this->belongsTo('App\Order');
    }
}
