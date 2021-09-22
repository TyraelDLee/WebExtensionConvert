/***
 * Copyright (c) 2021 Tyrael, Y. LI
 * */

browser.windows.onFocusChanged.addListener(function (wID){if(wID!==-1) lastWID = wID;});
browser.runtime.onInstalled.addListener(function (obj){
    // init setting
    browser.storage.sync.set({"notification": true}, function(){NOTIFICATION_PUSH = true;});
    browser.storage.sync.set({"medal": true}, function(){});
    browser.storage.sync.set({"checkIn": true}, function(){CHECKIN_ON = true;});
    browser.storage.sync.set({"imageNotice": false}, function(){IMAGE_NOTIFICATION = false;});
    browser.tabs.create({url: "./readme.html"});
});


browser.storage.onChanged.addListener(function (changes, namespace) {
    for (let [key, {oldValue, newValue}] of Object.entries(changes)) {
        if(key === "notification") NOTIFICATION_PUSH = newValue;
        if(key === "checkIn") CHECKIN_ON = newValue;
        if(key === "imageNotice")IMAGE_NOTIFICATION = newValue;
    }
});

function pushNotificationChrome(roomTitle, liverName, roomUrl, cover, type, face){
    let uid = Math.random();
    if(IMAGE_NOTIFICATION){
        browser.notifications.create(uid+":"+roomUrl, {}, function (id) {notificationClickHandler(id);});
    }else{
        browser.notifications.create(uid+":"+roomUrl, {}, function (id) {notificationClickHandler(id);});
    }
}


function reloadCookies() {
    browser.cookies.get({url: '', name: ''},
        function (SD) {});
    browser.cookies.get({url: '', name: ''},
        function (jct) {(jct === null)?JCT=-1:JCT = jct.value;});
}

browser.runtime.onMessage.addListener(function(request, sender, sendResponse){});

function notificationClickHandler(id){
    browser.notifications.onClicked.addListener(function (nid) {
        if (nid === id) {
            browser.windows.getAll(function (wins){
                if(wins.length>0){
                    // why google did not fix this bug over 6 years? WTF
                    browser.windows.getLastFocused(function (Lwin){});
                    browser.windows.update();
                    browser.tabs.create();
                }else
                    browser.windows.create();
            });
            browser.notifications.clear(id);
        }
    });
}

function loadSetting(){
    browser.storage.sync.get([], function(result){});
}

browser.alarm.clear(function (){});
browser.alarm.clearAll(function (){});
browser.alarm.create(function (){});
browser.alarm.get(function (){});
browser.alarm.getAll(function (){});
browser.alarm.onAlarm(function (){});

browser.bookmarks.create();
browser.bookmarks.get();
browser.bookmarks.getChildren();
browser.bookmarks.getRecent();
browser.bookmarks.getSubTree();
browser.bookmarks.onChildrenReordered();
browser.bookmarks.onImportBegan();

browser.browserAction.getBadgeTextColor();
browser.browserSettings.cacheEnabled();

browser.commands.getAll();
browser.commands.reset();

browser.extension.getURL();

browser.enterprise.deviceAttributes.get();
browser.enterprise.platformKeys.get();
