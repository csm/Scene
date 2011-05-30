//
//  MainViewController.h
//  Scene
//
//  Created by Casey Marshall on 5/28/11.
//  Copyright 2011 Modal Domains. All rights reserved.
//

#import "FlipsideViewController.h"

@interface MainViewController : UIViewController <FlipsideViewControllerDelegate> {
    UIImageView *splashImage;
    UILabel *lastPostLabel;
    UILabel *lastPostDetailLabel;
}

@property (retain, nonatomic) IBOutlet UIImageView *splashImage;
@property (retain, nonatomic) IBOutlet UILabel *lastPostLabel;
@property (retain, nonatomic) IBOutlet UILabel *lastPostDetailLabel;

- (IBAction)showInfo:(id)sender;

@end
