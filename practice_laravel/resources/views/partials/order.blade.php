<div class="row justify-content-center">
    <div class="col-12 col-lg-10">
        <div class="alert alert-warning">

            <h1 class="text-center">訂購產品</h1>


            <form id="Billing" name="Billing" class="form-horizontal" action="{{ action('ProductController@newOrder', ['product_name'=>$product_name]) }}" method="post">
                {!! csrf_field() !!}
                <div class="form-inline justify-content-center">

                    <div id="productname" class="col-4 text-right" data-price="1500">
                        <h4>這是產品名稱</h4>
                    </div>

                    <div class="col-4 text-center">
                        <div class="btn-group" role="group" aria-label="Basic example">
                            <input id="ProductMinus" type="button" value="-" class="btn btn-warning">

                            <input id="values" type="text" value="1" name="values" size="4">

                            <input id="ProductPlus" type="button" value="+" class="btn btn-warning">
                        </div>
                    </div>

                    <div class="col-4">
                        <h3 class="text-danger">NTD $<span name="price" id="price">{{$products->price}}</span></h3>
                    </div>

                </div>
                <hr>

                <h3>訂購人資訊</h3>

                <div class="form-group-inline">
                    <label for="name" class="col-sm-3 col-md-2 form-control-label">訂購人：</label>

                    <input type="text" id="name" name="name" placeholder="請填寫訂購人姓名" value="" class="col-4">

                </div>

                <div class="form-group-inline">
                    <label for="cellphone" class="col-sm-3 col-md-2 form-control-label">連絡手機：</label>

                    <input type="text" id="cellphone" name="cellphone" placeholder="0912-345678" value="" class="col-4">

                </div>

                <div class="form-group-inline">
                    <label for="email" class="col-sm-3 col-md-2">電子信箱：</label>

                    <input type="email" id="email" name="email" placeholder="請填寫您常用的email以利查詢訂單狀態" value="" class="col-8">

                </div>

                <div class="form-group-inline">
                    <label for="address" class="col-sm-3 col-md-2">地址：</label>
                    <input type="text" id="address" name="address" placeholder="請填寫您的詳細地址"value="" class="col-8">
                </div>

                <div class="form-inline">

                    <div class="col-sm-3 col-md-2">
                        付款方式：
                    </div>

                    <label class="form-check-label">
                        <input type="radio" id="payment_way" class="form-check-input" name="payment_way" value="貨到付款" checked=""> 貨到付款
                    </label>

                    <label class="form-check-label">
                        <input type="radio" id="payment_way" class="form-check-input" name="payment_way" value="ATM轉帳付款"> ATM轉帳付款
                    </label>

                </div>

                <div class="form-group-inline">
                    <label for="note" class="col-sm-3 col-md-2 align-top">備註：</label>
                    <textarea id="note" name="note" class="col-8" rows="5"></textarea>
                </div>

                <div class="col-xs">
                    <h4>匯款需知</h4>
                    <p>離島地區目前尚無貨到付款服務，在收到您的訂單後，我們的客服人員會主動撥電話與您確認訂單內容。確認後，請在到貨日三天前(不含假日)完成匯款至下列帳號並來電告知服務人員。其餘地區均可貨到付款。<br>
                        XXXX銀行() XXX分行<br>
                        XXXX有限公司<br>
                        帳號：XXXXXXXXXXXXX<br>
                        完成匯款後煩請來電告知您的匯款帳號後5碼。謝謝您的訂購。</p>
                    <div class="form-check">
                        <label class="form-check-label">
                            <input type="checkbox" checked="checked" class="form-check-input" name="AgreeCheckbox" id="AgreeCheckbox" value="agree">我同意以上須知
                        </label>
                    </div>
                </div>

                <button type="submit" class="btn btn-primary btn-lg btn-block glyphicon glyphicon-shopping-cart" aria-hidden="true">購買</button>
            </form>

        </div>
    </div>
</div>