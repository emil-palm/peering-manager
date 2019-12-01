from django.conf.urls import re_path
from . import views

app_name = "peering"

urlpatterns = [
    # Autonomous Systems
    re_path(
        r"^autonomous-systems/$", views.ASList.as_view(), name="autonomous_system_list"
    ),
    re_path(
        r"^autonomous-systems/add/$",
        views.ASAdd.as_view(),
        name="autonomous_system_add",
    ),
    re_path(
        r"^autonomous-systems/(?P<asn>[0-9]+)/$",
        views.ASDetails.as_view(),
        name="autonomous_system_details",
    ),
    re_path(
        r"^autonomous-systems/(?P<asn>[0-9]+)/edit/$",
        views.ASEdit.as_view(),
        name="autonomous_system_edit",
    ),
    re_path(
        r"^autonomous-systems/(?P<asn>[0-9]+)/email/$",
        views.ASEmail.as_view(),
        name="autonomous_system_email",
    ),
    re_path(
        r"^autonomous-systems/(?P<asn>[0-9]+)/delete/$",
        views.ASDelete.as_view(),
        name="autonomous_system_delete",
    ),
    re_path(
        r"^autonomous-systems/delete/$",
        views.ASBulkDelete.as_view(),
        name="autonomous_system_bulk_delete",
    ),
    re_path(
        r"^autonomous-systems/(?P<asn>[0-9]+)/direct-peering-sessions/$",
        views.AutonomousSystemDirectPeeringSessions.as_view(),
        name="autonomous_system_direct_peering_sessions",
    ),
    re_path(
        r"^autonomous-systems/(?P<asn>[0-9]+)/ix-peering-sessions/$",
        views.AutonomousSystemInternetExchangesPeeringSessions.as_view(),
        name="autonomous_system_internet_exchange_peering_sessions",
    ),
    re_path(
        r"^autonomous-systems/(?P<asn>[0-9]+)/contacts/$",
        views.AutonomousSystemContacts.as_view(),
        name="autonomous_system_contacts",
    ),
    # BGP Groups
    re_path(r"^bgp-groups/$", views.BGPGroupList.as_view(), name="bgp_group_list"),
    re_path(r"^bgp-groups/add/$", views.BGPGroupAdd.as_view(), name="bgp_group_add"),
    re_path(
        r"^bgp-groups/delete/$",
        views.BGPGroupBulkDelete.as_view(),
        name="bgp_group_bulk_delete",
    ),
    re_path(
        r"^bgp-groups/edit/$",
        views.BGPGroupBulkEdit.as_view(),
        name="bgp_group_bulk_edit",
    ),
    re_path(
        r"^bgp-groups/(?P<slug>[\w-]+)/$",
        views.BGPGroupDetails.as_view(),
        name="bgp_group_details",
    ),
    re_path(
        r"^bgp-groups/(?P<slug>[\w-]+)/edit/$",
        views.BGPGroupEdit.as_view(),
        name="bgp_group_edit",
    ),
    re_path(
        r"^bgp-groups/(?P<slug>[\w-]+)/delete/$",
        views.BGPGroupDelete.as_view(),
        name="bgp_group_delete",
    ),
    re_path(
        r"^bgp-groups/(?P<slug>[\w-]+)/peering-sessions/$",
        views.BGPGroupPeeringSessions.as_view(),
        name="bgp_group_peering_sessions",
    ),
    re_path(
        r"^bgp-groups/(?P<slug>[\w-]+)/add-peering-session/$",
        views.BGPGroupPeeringSessionAdd.as_view(),
        name="bgp_group_peering_session_add",
    ),
    # BGP Communities
    re_path(r"^communities/$", views.CommunityList.as_view(), name="community_list"),
    re_path(r"^communities/add/$", views.CommunityAdd.as_view(), name="community_add"),
    re_path(
        r"^communities/(?P<pk>[0-9]+)/$",
        views.CommunityDetails.as_view(),
        name="community_details",
    ),
    re_path(
        r"^communities/(?P<pk>[0-9]+)/edit/$",
        views.CommunityEdit.as_view(),
        name="community_edit",
    ),
    re_path(
        r"^communities/(?P<pk>[0-9]+)/delete/$",
        views.CommunityDelete.as_view(),
        name="community_delete",
    ),
    re_path(
        r"^communities/delete/$",
        views.CommunityBulkDelete.as_view(),
        name="community_bulk_delete",
    ),
    re_path(
        r"^communities/edit/$",
        views.CommunityBulkEdit.as_view(),
        name="community_bulk_edit",
    ),
    # Direct Peering Sessions
    re_path(
        r"^direct-peering-sessions/$",
        views.DirectPeeringSessionList.as_view(),
        name="direct_peering_session_list",
    ),
    re_path(
        r"^direct-peering-sessions/(?P<pk>[0-9]+)/$",
        views.DirectPeeringSessionDetails.as_view(),
        name="direct_peering_session_details",
    ),
    re_path(
        r"^direct-peering-sessions/add/(?P<asn>[0-9]+)/$",
        views.DirectPeeringSessionAdd.as_view(),
        name="direct_peering_session_add",
    ),
    re_path(
        r"^direct-peering-sessions/edit/$",
        views.DirectPeeringSessionBulkEdit.as_view(),
        name="direct_peering_session_bulk_edit",
    ),
    re_path(
        r"^direct-peering-sessions/delete/$",
        views.DirectPeeringSessionBulkDelete.as_view(),
        name="direct_peering_session_bulk_delete",
    ),
    re_path(
        r"^direct-peering-sessions/(?P<pk>[0-9]+)/edit/$",
        views.DirectPeeringSessionEdit.as_view(),
        name="direct_peering_session_edit",
    ),
    re_path(
        r"^direct-peering-sessions/(?P<pk>[0-9]+)/delete/$",
        views.DirectPeeringSessionDelete.as_view(),
        name="direct_peering_session_delete",
    ),
    re_path(
        r"^direct-peering-sessions/(?P<pk>[0-9]+)/disable/$",
        views.DirectPeeringSessionDisable.as_view(),
        name="direct_peering_session_disable",
    ),
    re_path(
        r"^direct-peering-sessions/(?P<pk>[0-9]+)/enable/$",
        views.DirectPeeringSessionEnable.as_view(),
        name="direct_peering_session_enable",
    ),
    # Internet Exchanges
    re_path(
        r"^internet-exchanges/$",
        views.InternetExchangeList.as_view(),
        name="internet_exchange_list",
    ),
    re_path(
        r"^internet-exchanges/add/$",
        views.InternetExchangeAdd.as_view(),
        name="internet_exchange_add",
    ),
    re_path(
        r"^internet-exchanges/peeringdb-import/$",
        views.InternetExchangePeeringDBImport.as_view(),
        name="internet_exchange_peeringdb_import",
    ),
    re_path(
        r"^internet-exchanges/delete/$",
        views.InternetExchangeBulkDelete.as_view(),
        name="internet_exchange_bulk_delete",
    ),
    re_path(
        r"^internet-exchanges/edit/$",
        views.InternetExchangeBulkEdit.as_view(),
        name="internet_exchange_bulk_edit",
    ),
    re_path(
        r"^internet-exchanges/(?P<slug>[\w-]+)/$",
        views.InternetExchangeDetails.as_view(),
        name="internet_exchange_details",
    ),
    re_path(
        r"^internet-exchanges/(?P<slug>[\w-]+)/edit/$",
        views.InternetExchangeEdit.as_view(),
        name="internet_exchange_edit",
    ),
    re_path(
        r"^internet-exchanges/(?P<slug>[\w-]+)/delete/$",
        views.InternetExchangeDelete.as_view(),
        name="internet_exchange_delete",
    ),
    re_path(
        r"^internet-exchanges/(?P<slug>[\w-]+)/add-peering-session/$",
        views.InternetExchangePeeringSessionAdd.as_view(),
        name="internet_exchange_peering_session_add",
    ),
    re_path(
        r"^internet-exchanges/(?P<slug>[\w-]+)/peering-sessions/$",
        views.InternetExchangePeeringSessions.as_view(),
        name="internet_exchange_peering_sessions",
    ),
    re_path(
        r"^internet-exchanges/(?P<slug>[\w-]+)/peers/$",
        views.InternetExchangePeers.as_view(),
        name="internet_exchange_peers",
    ),
    # Internet Exchange Peering Sessions
    re_path(
        r"^internet-exchange-peering-sessions/$",
        views.InternetExchangePeeringSessionList.as_view(),
        name="internet_exchange_peering_session_list",
    ),
    re_path(
        r"^internet-exchange-peering-sessions/(?P<pk>[0-9]+)/$",
        views.InternetExchangePeeringSessionDetails.as_view(),
        name="internet_exchange_peering_session_details",
    ),
    re_path(
        r"^internet-exchange-peering-sessions/(?P<pk>[0-9]+)/edit/$",
        views.InternetExchangePeeringSessionEdit.as_view(),
        name="internet_exchange_peering_session_edit",
    ),
    re_path(
        r"^internet-exchange-peering-sessions/(?P<pk>[0-9]+)/delete/$",
        views.InternetExchangePeeringSessionDelete.as_view(),
        name="internet_exchange_peering_session_delete",
    ),
    re_path(
        r"^internet-exchange-peering-sessions/add_from_peeringdb/$",
        views.InternetExchangePeeringSessionAddFromPeeringDB.as_view(),
        name="internet_exchange_peering_session_add_from_peeringdb",
    ),
    re_path(
        r"^internet-exchange-peering-sessions/edit/$",
        views.InternetExchangePeeringSessionBulkEdit.as_view(),
        name="internet_exchange_peering_session_bulk_edit",
    ),
    re_path(
        r"^internet-exchange-peering-sessions/delete/$",
        views.InternetExchangePeeringSessionBulkDelete.as_view(),
        name="internet_exchange_peering_session_bulk_delete",
    ),
    re_path(
        r"^internet-exchange-peering-sessions/(?P<pk>[0-9]+)/disable/$",
        views.InternetExchangePeeringSessionDisable.as_view(),
        name="internet_exchange_peering_session_disable",
    ),
    re_path(
        r"^internet-exchange-peering-sessions/(?P<pk>[0-9]+)/enable/$",
        views.InternetExchangePeeringSessionEnable.as_view(),
        name="internet_exchange_peering_session_enable",
    ),
    # Routers
    re_path(r"^routers/$", views.RouterList.as_view(), name="router_list"),
    re_path(r"^routers/add/$", views.RouterAdd.as_view(), name="router_add"),
    re_path(
        r"^routers/(?P<pk>[0-9]+)/$",
        views.RouterDetails.as_view(),
        name="router_details",
    ),
    re_path(
        r"^routers/(?P<pk>[0-9]+)/configuration/$",
        views.RouterConfiguration.as_view(),
        name="router_configuration",
    ),
    re_path(
        r"^routers/(?P<pk>[0-9]+)/edit/$",
        views.RouterEdit.as_view(),
        name="router_edit",
    ),
    re_path(
        r"^routers/(?P<pk>[0-9]+)/delete/$",
        views.RouterDelete.as_view(),
        name="router_delete",
    ),
    re_path(
        r"^routers/delete/$",
        views.RouterBulkDelete.as_view(),
        name="router_bulk_delete",
    ),
    re_path(
        r"^routers/edit/$", views.RouterBulkEdit.as_view(), name="router_bulk_edit"
    ),
    # Routing Policies
    re_path(
        r"^routing-policies/$",
        views.RoutingPolicyList.as_view(),
        name="routing_policy_list",
    ),
    re_path(
        r"^routing-policies/add/$",
        views.RoutingPolicyAdd.as_view(),
        name="routing_policy_add",
    ),
    re_path(
        r"^routing-policies/(?P<pk>[0-9]+)/$",
        views.RoutingPolicyDetails.as_view(),
        name="routing_policy_details",
    ),
    re_path(
        r"^routing-policies/(?P<pk>[0-9]+)/edit/$",
        views.RoutingPolicyEdit.as_view(),
        name="routing_policy_edit",
    ),
    re_path(
        r"^routing-policies/(?P<pk>[0-9]+)/delete/$",
        views.RoutingPolicyDelete.as_view(),
        name="routing_policy_delete",
    ),
    re_path(
        r"^routing-policies/delete/$",
        views.RoutingPolicyBulkDelete.as_view(),
        name="routing_policy_bulk_delete",
    ),
    re_path(
        r"^routing-policies/edit/$",
        views.RoutingPolicyBulkEdit.as_view(),
        name="routing_policy_bulk_edit",
    ),
    # Templates
    re_path(r"^templates/$", views.TemplateList.as_view(), name="template_list"),
    re_path(r"^templates/add/$", views.TemplateAdd.as_view(), name="template_add"),
    re_path(
        r"^templates/(?P<pk>[0-9]+)/$",
        views.TemplateDetails.as_view(),
        name="template_details",
    ),
    re_path(
        r"^templates/(?P<pk>[0-9]+)/edit/$",
        views.TemplateEdit.as_view(),
        name="template_edit",
    ),
    re_path(
        r"^templates/(?P<pk>[0-9]+)/delete/$",
        views.TemplateDelete.as_view(),
        name="template_delete",
    ),
    re_path(
        r"^templates/delete/$",
        views.TemplateBulkDelete.as_view(),
        name="template_bulk_delete",
    ),
]
