var city = form["city"].value;

var settings = {
  "async": true,
  "crossDomain": true,
  "url": "https://app.ticketmaster.com/discovery/v2/events/city.json?apikey=" + ticketmaster_key,
  "method": "GET",
  "headers": {
    "User-Agent": "PostmanRuntime/7.18.0",
    "Accept": "*/*",
    "Cache-Control": "no-cache",
    "Postman-Token": "edae6893-746f-4e52-967a-0d35c25df7f5,7352f812-6d62-4c64-85c4-af044f9be343",
    "Host": "app.ticketmaster.com",
    "Accept-Encoding": "gzip, deflate",
    "Cookie": "TMSO=seed=590e9c63ce0b&exp=1571683077&kid=key1&sig=0x841f9b8cf93705022eb7cdf3aa9f5317341af5cbf9fe6152689eccd3f63ff408b8fd79cee48c53876e69824be2c5458cb2ab91e366baddf5d8bd9584195b62a5",
    "Connection": "keep-alive",
    "cache-control": "no-cache"
  }
}

$.ajax(settings).done(function (response) {
  console.log(response);
});

