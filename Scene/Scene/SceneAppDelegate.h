//
//  SceneAppDelegate.h
//  Scene
//
//  Created by Casey Marshall on 5/28/11.
//  Copyright 2011 Modal Domains. All rights reserved.
//

#import <UIKit/UIKit.h>
#import <CoreLocation/CoreLocation.h>

@class MainViewController;

@interface SceneAppDelegate : NSObject <UIApplicationDelegate, CLLocationManagerDelegate>
{
    CLLocationManager *locationManager;
    CLLocation *location;
}

+ (SceneAppDelegate *) sharedDelegate;

@property (nonatomic, retain) IBOutlet UIWindow *window;

@property (nonatomic, retain) IBOutlet MainViewController *mainViewController;

@property (nonatomic, retain) CLLocation *location;

@end
