<!doctype html>
<html lang="zh-TW">
<head>
    <title>@yield('title')</title>
    @section('head')
        @include('partials.head')
    @show
</head>
<body>

    <div class="container">
        @yield('content')
    </div>

    <div class="order">
        @section('order')
            @include('partials.order')
        @show
    </div>

    @section('footer')
        @include('partials.footer')
    @show
</body>
</html>
