 @extends('layouts.master')

 @section('title', '快速帳篷')

 @section('content')

<div class="container-fluid">
		<div class="row justify-content-center">
			<div class="col-12 col-lg-10">

			
				<div class="jumbotron" style="background-color: #FFF">
	                <div class="page-header">
						<h1 class="text-center">
							拍賣商城限時特價中
						</h1>
					</div>

                    @foreach($pictures as $picture)
	                <img src="../img/{{$picture->picture_name}}" alt="" style="width:100%">

                    @endforeach

		    		<div class="embed-responsive embed-responsive-16by9">
					  <iframe class="embed-responsive-item" src="https://www.youtube.com/embed/sG6bmovdNhw" allowfullscreen></iframe>
					</div>
					<br>
					<blockquote class="blockquote">
				        <p class="">產品介紹...</p>
					</blockquote>
				
				</div>

			</div>
		</div>


	</div>

@stop
