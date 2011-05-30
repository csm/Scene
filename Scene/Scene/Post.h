//
//  Post.h
//  Scene
//
//  Created by Casey Marshall on 5/28/11.
//  Copyright 2011 Modal Domains. All rights reserved.
//

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
