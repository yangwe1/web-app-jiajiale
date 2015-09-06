from django.conf.urls import patterns,url
import indexViews,saleViews,rentViews,saleDetailViews,rentDetailViews,wantSaleViews,wantRentViews

urlpatterns = patterns('',
    url( r'^$', indexViews.showIndex.as_view(), name='index'),
    url( r'^qiu$', indexViews.showQiu.as_view() ),
    url( r'^contact$', indexViews.showContact.as_view() ),
    url( r'^sale/$', saleViews.getSaleList.as_view() ),
    url( r'^saleDetail/$', saleDetailViews.getEachDetailInfo.as_view() ),
    url( r'^rentDetail/$', rentDetailViews.getEachDetailInfo.as_view() ),
    url( r'^wantSale/$', wantSaleViews.sale.as_view() ),
    url( r'^wantRent/$', wantRentViews.sale.as_view() ),
    url( r'^rent/$', rentViews.getRentList.as_view() ),
)
