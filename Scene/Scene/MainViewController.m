//
//  MainViewController.m
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

#import "MainViewController.h"

@implementation MainViewController

@synthesize splashImage;
@synthesize lastPostLabel;
@synthesize lastPostDetailLabel;

/*
// Implement viewDidLoad to do additional setup after loading the view, typically from a nib.
- (void)viewDidLoad
{
    [super viewDidLoad];
}
*/

- (void) fadeOutSplashImageAnimation: (NSString *) animationId
                            finished: (BOOL) finished
                             context: (void *) context
{
    [self.splashImage removeFromSuperview];
    self.splashImage = nil;
}

- (void) viewDidLoad
{
    [super viewDidLoad];
    [self.lastPostLabel setFont: [UIFont fontWithName: @"DroidSans"
                                                 size: 17]];
    [self.lastPostDetailLabel setFont: [UIFont fontWithName: @"DroidSans"
                                                       size: 13]];
}

- (void) viewDidAppear:(BOOL)animated
{
    [super viewDidAppear: animated];
    if (self.splashImage != nil)
    {
        [UIView beginAnimations: @"FadeOutSplashImage"
                        context: nil];
        [UIView setAnimationCurve: UIViewAnimationCurveEaseIn];
        [UIView setAnimationDuration: 1.0];
        [UIView setAnimationDelegate: self];
        [UIView setAnimationDidStopSelector: @selector(fadeOutSplashImageAnimation:finished:context:)];
        self.splashImage.alpha = 0;
        [UIView commitAnimations];
    }
}

- (void)flipsideViewControllerDidFinish:(FlipsideViewController *)controller
{
    [self dismissModalViewControllerAnimated:YES];
}

- (IBAction)showInfo:(id)sender
{    
    FlipsideViewController *controller = [[FlipsideViewController alloc] initWithNibName:@"FlipsideView" bundle:nil];
    controller.delegate = self;
    
    controller.modalTransitionStyle = UIModalTransitionStylePartialCurl;
    [self presentModalViewController:controller animated:YES];
    
    [controller release];
}

- (BOOL)shouldAutorotateToInterfaceOrientation:(UIInterfaceOrientation)interfaceOrientation
{
    // Return YES for supported orientations.
    return (interfaceOrientation == UIInterfaceOrientationPortrait);
}

- (void)didReceiveMemoryWarning
{
    // Releases the view if it doesn't have a superview.
    [super didReceiveMemoryWarning];
    
    // Release any cached data, images, etc. that aren't in use.
}

- (void)viewDidUnload
{
    [super viewDidUnload];

    // Release any retained subviews of the main view.
    // e.g. self.myOutlet = nil;
}

- (void)dealloc
{
    [super dealloc];
}

@end
