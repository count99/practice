<?php

namespace App;

use Illuminate\Database\Eloquent\Model;

class Picture extends Model
{
    protected $table = 'pictures';

    public function picture(){
        return $this->belongsTo('App\Product');
    }
}
