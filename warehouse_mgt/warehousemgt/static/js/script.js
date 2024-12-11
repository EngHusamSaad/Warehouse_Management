// $(document).ready(function () {
//     // التعامل مع الروابط في الشريط الجانبي
//     $('#sidebar a').on('click', function (e) {
//         e.preventDefault(); // منع التحميل الافتراضي للرابط
//         var url = $(this).data('url'); // الحصول على رابط الـ URL من خاصية data-url

//         // إجراء طلب AJAX
//         $.ajax({
//             url: url,
//             type: 'GET',
//             success: function (response) {
//                 $('#content').html(response); // تحديث القسم الرئيسي بالمحتوى
//             },
//             error: function () {
//                 alert('Error loading content.');
//             }
//         });
//     });
// });

// $.ajax({
//     url: url,
//     type: 'GET',
//     beforeSend: function () {
//         $('#content').html('<p>Loading...</p>');
//     },
//     success: function (response) {
//         $('#content').html(response);
//     },
//     error: function () {
//         $('#content').html('<p>Error loading content.</p>');
//     }
// });


$('#myModal').modal(options)
