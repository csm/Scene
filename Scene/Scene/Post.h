//
//  Post.h
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

#import <Foundation/Foundation.h>
#import <CoreLocation/CoreLocation.h>

#define kPostKeyDictKey      @"k"
#define kPostDateDictKey     @"d"
#define kPostMessageDictKey  @"m"
#define kPostLocationDictKey @"l"
#define kPostNameDictKey     @"n"
#define kPostAvatarDictKey   @"a"

@interface Post : NSObject
{
    NSString *key;
    NSDate *date;
    NSString *message;
    CLLocationCoordinate2D location;
    NSString *who;
    NSString *avatarId;
    UIImage *avatar;
}

@property (retain, nonatomic) NSString *key;
@property (retain, nonatomic) NSDate *date;
@property (retain, nonatomic) NSString *message;
@property (assign, nonatomic) CLLocationCoordinate2D location;
@property (retain, nonatomic) NSString *who;
@property (retain, nonatomic) NSString *avatarId;
@property (retain, nonatomic) UIImage *avatar;

- (id) initWithDictionary: (NSDictionary *) dict;

@end
