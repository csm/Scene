//
//  SceneAppDelegate.h
//  Scene
//
//  Created by Casey Marshall on 5/28/11.
//  Copyright 2011 Modal Domains. All rights reserved.
//
// This program is free software: you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
// 
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.
// 
// You should have received a copy of the GNU General Public License
// along with this program.  If not, see <http://www.gnu.org/licenses/>.

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
